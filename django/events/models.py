from django.db import models
from accounts.models import User
from django.conf import settings
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    author_id = models.IntegerField(default=1)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=300)
    date_begin = models.DateTimeField(max_length=300)
    date_end = models.DateTimeField(max_length=300)
    icon = models.ImageField(
        upload_to="images/", default="/images/default_icon.png")
    image = models.ImageField(
        upload_to='images/', default="/images/default_image.png")
    STATUS = Choices(('ECV', _('En cours de validation')),
                     ('VAL', _('Validé')),
                     ('TER', _('Terminé')),)
    status = models.CharField(
        choices=STATUS, default=STATUS.ECV, max_length=20)

    def __str__(self):
        return self.title + " by " + str(self.author_id)


class Participation(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    Adherent = models.ForeignKey("Adherent", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title + "  |  " + self.Adherent.user.username


class Adherent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    isAdmin = models.BooleanField(default=False)
    picture = models.ImageField(
        upload_to="images/users/", default="images/default_icon.png")

    def __str__(self):
        return self.user.username
