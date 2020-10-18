from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    image = models.ImageField(upload_to='photos/S')
    image_name = models.CharField(max_length=50)
    image_caption = models.CharField(max_length=100, default='')
    likes = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.image_name


    def get_abs_url(self):
        return reverse ('home')    
    

    @classmethod
    def get_image_by_id(cls, img_id):
        img_got = cls.objects.get(id=img_id)
        return img_got

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_caption(self, new_cap):
        self.caption = new_cap
        self.save()    
class Comment(models.Model):
    comment = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
