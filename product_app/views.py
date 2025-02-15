from django.shortcuts import render, redirect

from product_app.forms import ProductForm
from product_app.models import ProductDetails


# Create your views here.
def index(request):
    products = ProductDetails.objects.all()
    return render(request,'index.html',{'products' : products})


def add_product(request):
    form = ProductForm()
    print(form)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'add_product.html',{'forms':form})


def delete_product(request,product_id):
    product = ProductDetails.objects.get(id=product_id)
    product.delete()
    return redirect('index')


def update_product_details(request,product_id):
    product = ProductDetails.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        form.save()
        return redirect('index')
    return render(request,'update_product_details.html',{'form':form})
