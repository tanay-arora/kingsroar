from django.db.models import fields
from rest_framework import serializers
from .models import *

class bannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = banner
        fields = ['title','image','url']

class box_bannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = box_banner
        fields = ['title','image','url']

class mini_bannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = mini_banner
        fields = ['title', 'image','url']
