from django.shortcuts import render # type: ignore
from blog.models import Post, Comment

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)