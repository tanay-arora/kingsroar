from django.conf.urls import url
from django.urls import include, path
from .views import *

urlpatterns = [
    path("categories/", categoryListview.as_view(), name="categories"),
    path("subcategories/", sub_categoryListview.as_view(), name="subcategories"),
    path("offers/", offersListview.as_view(), name="offers"),
    path("offers/<slug>/", offersDetailview.as_view(), name="offer slug"),
    path("products/", productListview.as_view(), name="all products"),
    path("products/<pk>/", productDetailview.as_view(), name="product id"),
]