from django import forms
from .models import Category, Service, Advertise

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['category', 'name', 'description', 'price', 'image']

class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ['image', 'image_type', 'location']