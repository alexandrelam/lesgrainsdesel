from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=300)
    date_begin = models.DateTimeField(max_length=300)
    date_end = models.DateTimeField(max_length=300)
    icon = models.ImageField(upload_to="images/", default="/images/default_icon.png")
    image = models.ImageField(upload_to='images/', default="/images/default_image.png")
    participation = models.IntegerField(default=0)

    def __str__(self):
        return self.title + " by " + self.author
