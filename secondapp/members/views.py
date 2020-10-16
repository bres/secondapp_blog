from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout



# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('blog:home')    
    else:
        form=RegisterForm()        
   
    return render(request,'members/registration/signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user
            user =form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:home')
    
    else:
        form=AuthenticationForm()
    return render(request,'members/registration/login.html',{'form':form })


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('blog:home')
