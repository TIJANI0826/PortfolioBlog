from django.db import models
from tinymce.models import HTMLField 
# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="img")

