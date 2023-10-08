from django.db.models import fields
from rest_framework import serializers
from .models import *

# minor details serializers
class productCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['title','slug']

class productSub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = sub_category
        fields = ['title','slug']

class productBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ['title','slug']

class specs_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = specs_list
        fields = ['key','value']

class specificationSerializer(serializers.ModelSerializer):
    content = specs_listSerializer(read_only=True,many=True)
    class Meta:
        model = specification
        fields = ['title','content']

class highlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = highlight
        fields = ['title']

# main details serializers
class segmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = segment
        fields = ['title','image','slug']

class sub_categorySerializer(serializers.ModelSerializer):
    segments = segmentSerializer(read_only=True, many=True)
    class Meta:
        model = sub_category
        fields = ['title','image','segments','slug']

class categorySerializer(serializers.ModelSerializer):
    sub_categories = sub_categorySerializer(read_only=True, many=True)
    class Meta:
        model = category
        fields = ['title','image','sub_categories','slug']

class brandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ['title','image','slug']

class productSerializer(serializers.ModelSerializer):
    brand = brandSerializer(read_only=True)
    class Meta:
        model = product
        fields = ['id','title','image','brand','mrp','price','discount']

class productDetailSerializer(serializers.ModelSerializer):
    brand = productBrandSerializer(read_only=True)
    sub_category = productSub_categorySerializer(read_only=True)
    category = productCategorySerializer(read_only=True)
    specification = specificationSerializer(read_only=True,many=True)
    highlight = highlightSerializer(read_only=True,many=True)
    class Meta:
        model = product
        fields = ['id','title','discount','category','sub_category','image','image1','quantity','highlight','description','specification','brand','mrp','price','discount']

# other serializers

class offerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = offer
        fields = ['title','slug']

class offerSerializer(serializers.ModelSerializer):
    products = productSerializer(read_only=True,many=True)
    class Meta:
        model = offer
        fields = ['title','slug','products']