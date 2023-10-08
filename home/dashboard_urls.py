from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name="dashboard"),
    path('banners/', banners, name="banners"),
    path('box-banners/', box_banners, name="box banners"),
    path('mini-banners/', mini_banners, name="mini banners"),
    path('categories/', categories, name="categories"),
    path('sub-categories/', sub_categories, name="sub categories"),
    path('segments/', segments, name="segments"),
    path('brands/', brands, name="brands"),
    path('category/<pk>', category_detail , name="single category"),
    path('sub-category/<pk>', subcategory_detail,  name="singel sub category"),
    path('brands/add/', new_brand, name="add brands"),
    path('categories/add/', new_category, name="add categorys" ),
    path('categories/<id>/change/', edit_category, name="edit categories"),
    path('sub-categories/add/', new_subcategory, name="add sub categorys" ),
    path('sub-categories/<id>/change/', edit_subcategory, name="edit sub categories"),
    path('brands/<id>/change/', edit_brand, name="edit brands"),
    path('segments/add/', new_segment, name="add segments"),
    path('segments/<id>/change/', edit_segment, name="edit segments"),
    path('<value>/add/', new_banners , name="add new banners"),
    path('<value>/<id>/change/', edit_banners , name="edit banners"),
]