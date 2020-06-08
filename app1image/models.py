from django.db import models
from PIL import Image
# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    ph=models.IntegerField()
    image=models.ImageField(upload_to='images')

    def save(self):
        super().save()
        img=Image.open(self.image.path)
        h,w=img.size
        if h>300 and w>300:
            img.thumbnail((200,200),Image.ANTIALIAS)
            img.save(self.image.path)