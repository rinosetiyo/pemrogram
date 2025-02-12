from django.shortcuts import render # type: ignore
from blog.models import Post, Comment, Category

# Create your views here.

def index(request):
    posts = Post.objects.all()
    featured_posts = Post.objects.filter(is_featured=True)
    tags = Post.tags.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
        'featured_posts': featured_posts,
    }
    return render(request, 'index.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    recent_posts = Post.objects.all().order_by('-created_at')[:3]
    comments = Comment.objects.filter(post=post, parent=None).order_by('-created_at')
    categories = Category.objects.all()
    comment_count = Comment.objects.filter(post=post).count()
    context = {
        'post': post,
        'comments': comments,
        'categories': categories,
        'comment_count': comment_count,
        'recent_posts': recent_posts,
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