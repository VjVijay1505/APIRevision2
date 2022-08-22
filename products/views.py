from django.shortcuts import render, redirect
from .models import ProductModel
from .forms import ProductForm

# Create your views here.
def home(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def add(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'products/add.html', context)

def view(request, pk):
    product = ProductModel.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products/view.html', context)

def edit(request, pk):
    product = ProductModel.objects.get(id=pk)
    form = ProductForm(instance=product)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'products/add.html', context)

def delete(request, pk):
    product = ProductModel.objects.get(id=pk)
    product.delete()
    return redirect('/')
    