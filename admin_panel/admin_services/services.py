from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Category, Service 
from admin_panel.forms import ServiceForm
from pocket_service.decorators import admin_required

@admin_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/dashboard/list-service.html', {'services': services})

@admin_required
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

@admin_required
def service_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'admin/dashboard/new-service.html', {'form': form, "categories": categories})

@admin_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'admin/dashboard/new-service.html', {'form': form, "categories": categories, "service": service})

@admin_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'service_confirm_delete.html', {'service': service})
