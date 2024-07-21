from django.db import models
from tinymce.models import HTMLField 
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="media")


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    # age_group = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name


