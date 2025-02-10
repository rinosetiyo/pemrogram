from django.shortcuts import render # type: ignore
from blog.models import Post, Comment, Category

# Create your views here.

def index(request):
    posts = Post.objects.all()
    tags = Post.tags.all()
    category = Category.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'category': category,
    }
    return render(request, 'index.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    comments = Comment.objects.filter(post=post, parent=None).order_by('-created_at')
    category = Category.objects.all()
    context = {
        'post': post,
        'comments': comments,
        'category': category,
    }
    return render(request, 'single-post.html', context)