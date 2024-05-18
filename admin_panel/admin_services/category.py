from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from admin_panel.models import Category 
from admin_panel.forms import CategoryForm
from vendor_panel.models import ShopCategory
from pocket_service.decorators import admin_required


@admin_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'admin/dashboard/list-category.html', {'categories': categories, "user" :request.user})

@admin_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

@admin_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'admin/dashboard/new-category.html', {'form': form})

@admin_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/dashboard/new-category.html', {'form': form, 'category': category})

@admin_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    associated_services = ShopCategory.objects.filter(category=category)
    associated_services.delete()
    category.delete()
    categories = Category.objects.all()
    return render(request, 'admin/dashboard/list-category.html', {'categories': categories})
