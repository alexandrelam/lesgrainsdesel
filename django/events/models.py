from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import User
from django.conf import settings
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from io import BytesIO
from PIL import Image
from django.core.files import File


class Event(models.Model):
    title = models.CharField(max_length=50)
    author_id = models.IntegerField(default=1)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=300)
    date_begin = models.DateTimeField(max_length=300)
    date_end = models.DateTimeField(max_length=300)
    odoo_id = models.IntegerField(default=-1)
    icon = models.ImageField(
        upload_to="images/", default="images/default_icon.png")
    image = models.ImageField(
        upload_to='images/', default="images/default_image.png")
    STATUS = Choices(('ECV', _('En cours de validation')),
                     ('VAL', _('Validé')),
                     ('TER', _('Terminé')),)
    status = models.CharField(
        choices=STATUS, default=STATUS.ECV, max_length=20)

    def compress(self, image):
        im = Image.open(image)
        im = im.convert('RGB')
        im_io = BytesIO()
        im.save(im_io, 'JPEG', quality=60)
        new_image = File(im_io, name=image.name)
        return new_image

    def save(self, *args, **kwargs):
        '''try to compress images and icons when uploaded'''
        print(f"THIS IS THE DEFAULT IMAGE :!!!!!!!!!!!! : {self.image}")
        if "default" not in self.image:
            new_image = self.compress(self.image)
            self.image = new_image

        if "default" not in self.icon:
            new_icon = self.compress(self.icon)
            self.icon = new_icon
        super().save(*args, **kwargs)


class Participation(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    Adherent = models.ForeignKey("Adherent", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title + "  |  " + str(self.Adherent.userId)


class Adherent(models.Model):
    userId = models.IntegerField(default=1)
    picture = models.ImageField(
        upload_to="images/users/", default="images/default_icon.png")

    def __str__(self):
        return str(self.userId)


@receiver(post_save, sender=User, dispatch_uid="login_user")
def create_adherent(sender, instance, **kwargs):
    if len(Adherent.objects.filter(userId=instance.userId)) == 0:
        adherent = Adherent()
        adherent.userId = instance.userId
        post_save.disconnect(create_adherent, sender=User)
        adherent.save()
        post_save.connect(create_adherent, sender=User)
        print("adherent created")
