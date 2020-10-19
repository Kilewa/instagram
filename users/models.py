from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    image_url = models.ImageField(default='default.jpg', upload_to='profile_pics')
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()  
        
        img = Post.open(self.image_url.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image_url.path)