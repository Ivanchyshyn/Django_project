from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm

def product_create_view(request):
    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            form = RawProductForm()
    else:
        form = RawProductForm()
    context = {
            'form': form
        }
    return render(request, "product/create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product/create.html", context)


def product_detail_view(request):
    context = {}
    if request.method == 'GET':
        queryset = Product.objects.all()
        context = {
            'object_list': queryset
        }
    return render(request, "product/detail.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "product/product-detail.html", context)