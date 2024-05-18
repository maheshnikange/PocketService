from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from admin_panel.models import Advertise, Category, Service
from vendor_panel.models import VendorService

def index(request):
    categories = Category.objects.all()
    advertise_images = Advertise.objects.filter(location='dashboard')
    return render(request,'index.html', {"advertise_images": advertise_images, "categories": categories})
    
def login(request):
    print("inside maina app-------------------------------")
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')


def get_admin_category_services(request, cat_id):
    services = Service.objects.filter(category_id=cat_id)
    return render(request,'shop-catergory-page.html', {"admin_services": services}) 

def get_service_shop(request,service_id):
    vendor_services = VendorService.objects.filter(service_id=service_id)
    return render(request,'vendor-shop-lists.html', {"shop_list": vendor_services}) 