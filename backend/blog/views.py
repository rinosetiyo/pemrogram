from django.shortcuts import render # type: ignore
from blog.models import Post, Comment, Category

# Create your views here.

def index(request):
    posts = Post.objects.all()
    tags = Post.tags.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    comments = Comment.objects.filter(post=post, parent=None).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'post': post,
        'comments': comments,
        'categories': categories,
    }
    return render(request, 'single-post.html', context)

def category(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'index.html', context)