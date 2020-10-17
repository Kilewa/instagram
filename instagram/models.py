from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=100)
    likes = models.IntegerField()
    comments = models.TextField()
