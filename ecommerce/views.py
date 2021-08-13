from django.shortcuts import render
from store.models import Product

def home(request):
    #do the query to display your products in your html file home page
    products = Product.objects.all().filter(is_available=True)

    #we got all the products from this product variable
    context = {
        'products': products,
        }
    return render(request, 'home.html', context)
