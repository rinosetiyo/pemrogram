from django.urls import path, include # type: ignore
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<post_slug>/', views.post_detail, name='post_detail'),
]