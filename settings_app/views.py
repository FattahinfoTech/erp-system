# settings_app/views.py (updated)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import ClusterZone, FinishProductType, CustomerCategory, EmailSetting
from .forms import ClusterZoneForm, FinishProductTypeForm, CustomerCategoryForm, EmailSettingForm

@login_required
def cluster_zone(request):
    clusters = ClusterZone.objects.all()
    
    if request.method == 'POST':
        # Handle create
        if 'cluster' in request.POST and 'zone' in request.POST:
            form = ClusterZoneForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cluster & Zone added successfully!')
                return redirect('cluster_zone')
        
        # Handle edit
        elif 'cluster_id' in request.POST:
            cluster_id = request.POST.get('cluster_id')
            cluster = get_object_or_404(ClusterZone, id=cluster_id)
            cluster.cluster = request.POST.get('cluster')
            cluster.zone = request.POST.get('zone')
            cluster.status = request.POST.get('status')
            cluster.save()
            messages.success(request, 'Cluster & Zone updated successfully!')
            return redirect('cluster_zone')
        
        # Handle delete
        elif 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            cluster = get_object_or_404(ClusterZone, id=delete_id)
            cluster.delete()
            messages.success(request, 'Cluster & Zone deleted successfully!')
            return redirect('cluster_zone')
    
    else:
        form = ClusterZoneForm()
    
    # Pagination
    paginator = Paginator(clusters, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'settings_app/cluster_zone.html', {
        'clusters': page_obj,
        'form': form
    })

@login_required
def finish_product_type(request):
    product_types = FinishProductType.objects.all()
    
    if request.method == 'POST':
        # Handle create
        if 'type_title' in request.POST and 'value' in request.POST:
            form = FinishProductTypeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product Type added successfully!')
                return redirect('finish_product_type')
        
        # Handle edit
        elif 'product_type_id' in request.POST:
            product_type_id = request.POST.get('product_type_id')
            product_type = get_object_or_404(FinishProductType, id=product_type_id)
            product_type.type_title = request.POST.get('type_title')
            product_type.value = request.POST.get('value')
            product_type.status = request.POST.get('status')
            product_type.save()
            messages.success(request, 'Product Type updated successfully!')
            return redirect('finish_product_type')
        
        # Handle delete
        elif 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            product_type = get_object_or_404(FinishProductType, id=delete_id)
            product_type.delete()
            messages.success(request, 'Product Type deleted successfully!')
            return redirect('finish_product_type')
    
    else:
        form = FinishProductTypeForm()
    
    return render(request, 'settings_app/finish_product_type.html', {
        'product_types': product_types,
        'form': form
    })

@login_required
def customer_category(request):
    categories = CustomerCategory.objects.all()
    
    if request.method == 'POST':
        # Handle create
        if 'category_title' in request.POST:
            form = CustomerCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Customer Category added successfully!')
                return redirect('customer_category')
        
        # Handle edit
        elif 'category_id' in request.POST:
            category_id = request.POST.get('category_id')
            category = get_object_or_404(CustomerCategory, id=category_id)
            category.category_title = request.POST.get('category_title')
            category.status = request.POST.get('status')
            category.save()
            messages.success(request, 'Customer Category updated successfully!')
            return redirect('customer_category')
        
        # Handle delete
        elif 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            category = get_object_or_404(CustomerCategory, id=delete_id)
            category.delete()
            messages.success(request, 'Customer Category deleted successfully!')
            return redirect('customer_category')
    
    else:
        form = CustomerCategoryForm()
    
    # Pagination
    paginator = Paginator(categories, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'settings_app/customer_category.html', {
        'categories': page_obj,
        'form': form
    })

@login_required
def email_setting(request):
    email_settings = EmailSetting.objects.all()
    
    if request.method == 'POST':
        # Handle create
        if 'type' in request.POST and 'emails' in request.POST:
            form = EmailSettingForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Email Setting added successfully!')
                return redirect('email_setting')
        
        # Handle edit
        elif 'email_id' in request.POST:
            email_id = request.POST.get('email_id')
            email_setting = get_object_or_404(EmailSetting, id=email_id)
            email_setting.type = request.POST.get('type')
            email_setting.emails = request.POST.get('emails')
            email_setting.status = request.POST.get('status')
            email_setting.save()
            messages.success(request, 'Email Setting updated successfully!')
            return redirect('email_setting')
        
        # Handle delete
        elif 'delete_id' in request.POST:
            delete_id = request.POST.get('delete_id')
            email_setting = get_object_or_404(EmailSetting, id=delete_id)
            email_setting.delete()
            messages.success(request, 'Email Setting deleted successfully!')
            return redirect('email_setting')
    
    else:
        form = EmailSettingForm()
    
    return render(request, 'settings_app/email_setting.html', {
        'email_settings': email_settings,
        'form': form
    })