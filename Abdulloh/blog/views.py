from .models import Post
from django.shortcuts import render

# Create your views here.


# Existing views for home and post_detail
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def post(request):
    return render(request, 'post.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def post1(request):
    return render(request, 'post1.html')


def post2(request):
    return render(request, 'post2.html')


def post3(request):
    return render(request, 'post3.html')