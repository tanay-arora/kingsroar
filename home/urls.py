from django.urls import include, path
from .views import *

urlpatterns = [
    path('banners/', bannerListview.as_view(), name="banners"),
    path('box_banners/', box_bannerListview.as_view(), name="box banners"),
    path('mini_banners/', mini_bannerListview.as_view(), name="mini banners")
]