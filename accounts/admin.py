from django.contrib import admin
from .models import *

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username','customer','seller','gender','last_login']
    search_fields = ['username']

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(godown)
class godownAdmin(admin.ModelAdmin):
    list_display = ['contact_person','mobile','gst_no','address']

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['user','otp','created']

@admin.register(seller)
class sellerAdmin(admin.ModelAdmin):
    list_display = ['name','company_name','pancard_no']