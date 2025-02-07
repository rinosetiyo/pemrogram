from django.urls import path, include # type: ignore
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
]