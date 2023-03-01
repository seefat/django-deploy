from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
# Create your views here.

def category_detail(request,slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    return render(request, 'store/category_detail.html',{
        'category':category,
        'products':products
    })


def product_detail(request, category_slug , slug):
    product = get_object_or_404(Product, slug=slug,status=Product.ACTIVE)
    return render(request, 'store/product_detail.html', {'product':product})

def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains = query) | Q(description__icontains = query))
    dic = {'query':query, 'products':products}
    return render(request, 'store/search.html',dic)
