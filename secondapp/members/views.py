from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')    
    else:
        form=RegisterForm()        
   
    return render(request,'members/registration/signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user
            return redirect('blog:home')
    
    else:
        form=AuthenticationForm()
    return render(request,'members/registration/login.html',{'form':form })
