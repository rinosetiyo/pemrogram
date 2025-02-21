from django.shortcuts import render # type: ignore
from shop.models import DigitalProduct # type: ignore

# Create your views here.
def shop(request):
    products = DigitalProduct.objects.filter(is_active=True)
    context = {
        'products': products
    }
    return render(request, 'products.html', context)