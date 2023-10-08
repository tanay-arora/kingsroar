from django.db import models
from django.contrib.auth.models import AbstractUser
from home.validators import clean_image
gender = [
    ('M',"Male"),
    ('F',"Female")
]
class User(AbstractUser):
    email = models.EmailField(null=True,blank=True)
    gender = models.CharField(max_length=1,null=True,blank=True,choices=gender)
    is_customer = models.BooleanField(default=False) # a customer 
    is_seller = models.BooleanField(default=False) # a seller
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.username

class OTP(models.Model):
    user = models.CharField(max_length=13)
    otp = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class customer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='customer')
    def __str__(self):
        return self.user.username

class seller(models.Model):
    name = models.CharField(max_length=25)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='seller')
    company_name = models.CharField(max_length=360)
    pancard_no = models.CharField(max_length=10,unique=True)
    pancard_image = models.ImageField(upload_to="users/pancards/",validators=[clean_image])
    def __str__(self):
        return self.name+": "+self.user.username

class godown(models.Model):
    seller = models.ForeignKey(seller, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=160)
    mobile = models.CharField(max_length=12)
    gst_no = models.CharField(max_length=15,unique=True)
    gst_certificate = models.ImageField(upload_to="users/gst_certificates/",validators=[clean_image])
    address = models.TextField()
    street = models.TextField()
    landmark = models.TextField(null=True,blank=True)
    def __str__(self) -> str:
        return self.contact_person+": "+self.mobile