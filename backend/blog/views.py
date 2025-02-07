from django.shortcuts import render # type: ignore
from blog.models import Post, Comment

# Create your views here.
def index(request):
    featured = Post.objects.filter(featured_blog=True)[0:2]
    context = {
        'featured': featured,
    }
    return render(request, 'index.html', context)