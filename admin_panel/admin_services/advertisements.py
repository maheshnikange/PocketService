from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Advertise
from admin_panel.forms import AdvertiseForm
from pocket_service.decorators import admin_required

@admin_required
def advertise_list(request):
    advertises = Advertise.objects.all()
    return render(request, 'admin/dashboard/list-advertise.html', {'advertises': advertises})

@admin_required
def advertise_detail(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    return render(request, 'advertise_detail.html', {'advertise': advertise})

@admin_required
def advertise_create(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('advertise_list')
    else:
        form = AdvertiseForm()
    return render(request, 'admin/dashboard/new-advertise.html', {'form': form})

@admin_required
def advertise_update(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    if request.method == 'POST':
        form = AdvertiseForm(request.POST, request.FILES, instance=advertise)
        if form.is_valid():
            form.save()
            return redirect('advertise_list')
    else:
        form = AdvertiseForm(instance=advertise)
    return render(request, 'admin/dashboard/new-advertise.html', {'form': form, "advertise": advertise})

@admin_required
def advertise_delete(request, pk):
    advertise = get_object_or_404(Advertise, pk=pk)
    if request.method == 'POST':
        advertise.delete()
        return redirect('advertise_list')
    return render(request, 'advertise_confirm_delete.html', {'advertise': advertise})
