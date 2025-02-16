from django.shortcuts import render # type: ignore
from blog.models import Post, Comment, Category
from blog.forms import CommentForm
from django.conf import settings # type: ignore

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
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
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            postid = request.POST.get('post_id')
            post = Post.objects.get(id=postid)
            comment.post = post
            content = request.POST.get('content')
            comment.content = content
            comment.save()

    context = {
        'post': post,
        'comments': comments,
        'categories': categories,
        'recent_posts': recent_posts,
        'comment_form': comment_form,
    }
    return render(request, 'blog-single.html', context)

def category(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'index.html', context)