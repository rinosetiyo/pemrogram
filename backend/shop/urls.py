from django.urls import path # type: ignore
from shop import views # type: ignore

urlpatterns = [
    path('', views.shop, name='shop'),
]