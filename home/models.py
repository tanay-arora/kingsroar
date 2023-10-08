from .validators import clean_image
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class banner(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="banner/",validators=[clean_image])
    url = models.CharField(max_length=160,null=True,blank=True)
    def __str__(self):
        return self.title

class box_banner(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="box_banner/",validators=[clean_image])
    url = models.CharField(max_length=160,null=True,blank=True)
    def __str__(self):
        return self.title

class mini_banner(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="mini_banner/",validators=[clean_image])
    url = models.CharField(max_length=160,null=True,blank=True)
    def __str__(self):
        return self.title
