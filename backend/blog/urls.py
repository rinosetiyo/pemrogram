from django.urls import path # type: ignore
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('category/<category_slug>/', views.category, name='category'),
    path('post/<post_slug>/', views.post_detail, name='post_detail'),
]