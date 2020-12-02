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

    def __str__(self):
        return self.title + " by " + self.author

class Participation(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    adherant = models.ForeignKey("Adherant", on_delete=models.CASCADE)

    def __str__(self):
        return self.event.title + " |  "  + self.adherant.name 


class Adherant(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="images/users/", default="images/default_icon.png")

    def __str__(self):
        return self.name
    
