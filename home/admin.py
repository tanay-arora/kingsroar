from django.contrib import admin
from .models import *

@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    list_display=['title','url']

@admin.register(box_banner)
class box_bannerAdmin(admin.ModelAdmin):
    list_display=['title','url']

@admin.register(mini_banner)
class mini_bannerAdmin(admin.ModelAdmin):
    list_display=['title','url']
