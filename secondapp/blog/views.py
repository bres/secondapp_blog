from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here

def index(request):
    return render(request,'index.html')

def postList(request):
    all_posts = Post.newmanager.all()
    return render(request,'postlist.html',{'post':all_posts})


def postSingle(request,slug):
    post=get_object_or_404(Post,slug=slug,status='published')
    return render(request,'postsingle.html',{'post':post})
