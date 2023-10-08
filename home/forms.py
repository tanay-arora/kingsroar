from products.models import segment, sub_category
from django import forms
from django.db import models
from .models import banner

status = [
    ("inreview","In review"),
    ("approved","Approved"),
    ("disapproved","Disapproved")
]

class bannerForm(forms.Form):
    title = forms.CharField(max_length=26,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control medium-file'}),required=False)
    url = forms.CharField(max_length=160,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)    

class brandForm(forms.Form):
    title = forms.CharField(max_length=26,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control medium-file'}),required=False)
    status = forms.ChoiceField(choices=status,initial="approved", widget=forms.Select(attrs={'class':'medium-select'}),required=False)
    admin_remarks = forms.CharField(widget=forms.Textarea(attrs={'class': 'mdl-textfield__input medium','rows':5}),required=False)

class categoryForm(forms.Form):
    title = forms.CharField(max_length=26,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control medium-file'}),required=False)
    sub_categories = forms.ModelMultipleChoiceField(
        queryset = sub_category.objects.all(),
        widget = forms.CheckboxSelectMultiple(),
    required=False)

class sub_categoryForm(forms.Form):
    title = forms.CharField(max_length=26,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control medium-file'}),required=False)
    segments = forms.ModelMultipleChoiceField(
        queryset = segment.objects.all(),
        widget = forms.CheckboxSelectMultiple(),
    required=False)

class segmentForm(forms.Form):
    title = forms.CharField(max_length=26,widget=forms.TextInput(attrs={'class': 'mdl-textfield__input medium'}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control medium-file'}),required=False)
