from django.contrib import admin
from .models import *

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

@admin.register(sub_category)
class sub_categoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

@admin.register(segment)
class sub_categoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
    list_display = ['title','slug','status']

@admin.register(specification)
class specificationAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(specs_list)
class specs_listAdmin(admin.ModelAdmin):
    list_display = ['key','value']

@admin.register(highlight)
class highlightAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(offer)
class offersAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ['title','category','sub_category','mrp','price']