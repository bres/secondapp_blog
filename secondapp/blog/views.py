from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here

def index(request):
    latest_post=Post.newmanager.first()
    return render(request,'blog/index.html',{'latest_post':latest_post})


def postList(request):
    all_posts = Post.newmanager.all()
    return render(request,'blog/postlist.html',{'post':all_posts})


def postSingle(request,slug):
    post=get_object_or_404(Post,slug=slug,status='published')
    return render(request,'blog/postsingle.html',{'post':post})


@login_required(login_url="/members/login/")
def create_post(request):
    form=PostForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.author=request.user
        instance.save()
        return redirect('blog:postlist')

    return render(request,'blog/create-form.html',{'form':form})

@login_required(login_url="/members/login/")
def update_post(request,slug):
    post=Post.objects.get(slug=slug)
    form=PostForm(request.POST or None,instance=post)

    if form.is_valid():
        form.save()
        return redirect('blog:postlist')
    return render(request,'blog/update-form.html',{'form':form,'post':post})

@login_required(login_url="/members/login/")
def delete_post(request,slug):
    post=Post.newmanager.get(slug=slug)

    if request.method=='POST':
        post.delete()
        return redirect ('blog:postlist')
    return render(request,'blog/post-delete.html',{'post':post})


def writersList(request):
    all_writers=User.objects.all()
    all_writer=Post.objects.all()
    return render(request,'blog/writers.html',{'all_writers':all_writers,'all_writer':all_writer})
