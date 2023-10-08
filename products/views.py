from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import *
from .models import *

class categoryListview(ListAPIView):
    serializer_class = categorySerializer
    queryset = category.objects.all()

class brandListview(ListAPIView):
    serializer_class = brandSerializer
    queryset = brand.objects.filter(status="approved")

class sub_categoryListview(ListAPIView):
    serializer_class = sub_categorySerializer
    queryset = sub_category.objects.all()

class offersListview(ListAPIView):
    serializer_class = offerListSerializer
    queryset = offer.objects.all()

class productListview(ListAPIView):
    serializer_class = productSerializer
    queryset = product.objects.filter(status="approved")

class productDetailview(RetrieveAPIView):
    serializer_class = productDetailSerializer
    queryset = product.objects.filter(status="approved")

class offersDetailview(ListAPIView):
    serializer_class = offerSerializer
    def get_queryset(self):
        query = self.kwargs.get('slug')
        queryset = offer.objects.filter(slug=query)
        return queryset