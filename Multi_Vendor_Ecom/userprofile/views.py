from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from store.models import Product, Category
from store.forms import ProductForm
from django.utils.text import slugify
from django.contrib import messages
#from django.http import HttpResponse

# Create your views here.



def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    dic = {'user': user,'products':products}
    return render(request, 'userprofile/vendor_detail.html', dic)
@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            messages.success(request, 'That Product is added successfully')
            return redirect('mystore')
    else:
        form = ProductForm()
    title = 'Edit Product'
    dic = {'form':form, 'title':title}
    return render(request, 'userprofile/product_form.html',dic)

@login_required
def mystore(request):
    products = request.user.products.exclude(status=Product.DELETED)
    dic = {'products':products}
    return render(request, 'userprofile/mystore.html',dic)


def signup(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = UserProfile.objects.create(user=user)
            return redirect('frontpage')

    else:
        form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def edit_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            messages.success(request, 'That Product is edited successfully')

            return redirect('mystore')
    else:
        form = ProductForm(instance=product)

    
    
    dic = {'form':form, 'title':'Edit Product', 'product':product}
    return render(request, 'userprofile/product_form.html',dic)


@login_required
def delete_product(request,pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = product.DELETED
    product.save()
    messages.success(request, 'Product is deleted')
    return redirect('mystore')