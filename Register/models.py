from django.db import models
from django.contrib.auth.models import User, Group
from PIL import Image

# Create your models here.

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to='profile_pics', null=True, default='pic.jpg')
    dob = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    father = models.CharField(max_length=100, null=True)
    mother = models.CharField(max_length=100, null=True)
    plus2name = models.CharField(max_length=100, null=True)
    plus2board = models.CharField(max_length=50, null=True)
    plus2year = models.CharField(max_length=10, null=True)
    plus2percent = models.CharField(max_length=10, null=True)
    slcname = models.CharField(max_length=100, null=True)
    slcboard = models.CharField(max_length=50, null=True)
    slcyear = models.CharField(max_length=10, null=True)
    slcpercent = models.CharField(max_length=10, null=True)
    glevel = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='profile_pics', null=True, default='pic.jpg')
    role = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)

    # to save image in small size
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height >300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return str(self.user)
