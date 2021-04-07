from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login,logout

def index(request):
    return render(request,'book-store/index.html')

def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/book-store')
    context={}
    return render(request,'book-store/signin.html',context)

	
	
def signUp(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/book-store/signIn")
    else:
        form=RegisterForm()
    return render(request,"book-store/signup.html",{"form":form})