from django.db import models # type: ignore
from django.conf import settings # type: ignore

User = settings.AUTH_USER_MODEL

class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Model representing a digital product (e.g., a ZIP file)
class DigitalProduct(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    cover_image = models.ImageField(upload_to='digital_products/cover', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='digital_products/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Model representing an order made by a user
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.user}"

# Model representing an order item associated with an order and a digital product
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(DigitalProduct, on_delete=models.CASCADE, related_name='order_items')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.title}"

# Model to track download attempts and limits for purchased digital products
# class Download(models.Model):
#     order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='downloads')
#     download_count = models.PositiveIntegerField(default=0)
#     max_downloads = models.PositiveIntegerField(default=3)
#     last_download = models.DateTimeField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def can_download(self):
#         return self.download_count < self.max_downloads

#     def __str__(self):
#         return f"Downloads for {self.order_item.product.title}"