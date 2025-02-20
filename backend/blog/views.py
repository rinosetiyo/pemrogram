from django.shortcuts import render, redirect # type: ignore
from blog.models import Post, Comment, Category
from shop.models import DigitalProduct, Order, CategoryProduct # type: ignore
from blog.forms import CommentForm
from django.http import JsonResponse # type: ignore
from django.conf import settings # type: ignore

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    digitals = DigitalProduct.objects.all().order_by('-created')[:3]
    context = {
        'posts': posts,
        'digitals': digitals,
    }
    return render(request, 'index.html', context)

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    recent_posts = Post.objects.all().order_by('-created_at')[:3]
    comments = Comment.objects.filter(post=post, parent=None).order_by('-created_at')
    categories = Category.objects.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_id = request.POST.get('parent')
            parent_obj = Comment.objects.filter(id=parent_id).first() if parent_id else None

            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_obj
            new_comment.save()

            return redirect('post_detail', post_slug=post_slug)


    # this is basic logic for comment reply, but it's not robust
    # 
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         parent_obj = None
    #         if request.POST.get('parent'):
    #             parent_obj = Comment.objects.get(id=request.POST.get('parent'))
    #             if parent_obj:
    #                 reply_comment = comment_form.save(commit=False)
    #                 reply_comment.parent = parent_obj
    #                 reply_comment.author = request.user
    #                 reply_comment.post = post
    #                 reply_comment.save()
    #                 return redirect('post_detail', post_slug=post_slug)
    #         else:
    #             comment = comment_form.save(commit=False)
    #             comment.author = request.user
    #             postid = request.POST.get('post_id')
    #             post = Post.objects.get(id=postid)
    #             comment.post = post
    #             content = request.POST.get('content')
    #             comment.content = content
    #             comment.save()

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