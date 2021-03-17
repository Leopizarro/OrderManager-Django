from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import RawProductForm


# Create your views here.

@login_required
def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form= RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form" : my_form
    }
    return render(request, "products/product_create.html", context)

@login_required
def product_detail_view(request):
    product = Product.objects.get(id=1)
    context = {
        "product": product
    }
    return render(request, "products/product_detail.html", context)

@login_required
def product_individual_view(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, "products/product_detail.html", context)

@login_required
def products_list_view(request):
    products_list = Product.objects.all() #lista de objetos
    user = request.user.id
    context= {
        'products_list': products_list,
        'userid': user
    }
    return render(request, "products/products_list.html", context)



