from django.shortcuts import render
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
        my_id = request.GET.get('id')
        if not my_id: my_id=1
        obj = Product.objects.get(id=my_id)
        context = {
            'object': obj,
            'length': len(Product.objects.all())
        }
    return render(request, "product/detail.html", context)