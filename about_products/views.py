from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'about_products/landing.html'
    )

def about_products(request):
    return render(
        request,
        'about_products/about_products.html'
    )