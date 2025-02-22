from django.shortcuts import render # type: ignore
from shop.models import DigitalProduct # type: ignore

# Create your views here.
def shop(request):
    products = DigitalProduct.objects.filter(is_active=True)
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def order(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        try:
            product = DigitalProduct.objects.get(pk=product_id, is_active=True)
            # Here you could create an Order record, process payment, etc.
            message = f"Order placed successfully for {product.name}."
        except DigitalProduct.DoesNotExist:
            message = "Product not found or inactive."
    else:
        message = "Please submit your order via POST."

    context = {'message': message}
    return render(request, 'order.html')