from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.template import loader
from .models import BookDetails


def index(request):
    book_list= BookDetails.objects.order_by('-timeAdded')
    book_list=book_list[0:3]
    first=book_list[0]
    second=book_list[1]
    third=book_list[2]
    #instead of sending the entire book list, try sending just 3. Each seperately
    template=loader.get_template('book-store/index.html')
    context={'book_list0':first,
    'book_list1':second,
    'book_list2':third,}
    #print ("Context= ", context)
    return HttpResponse(template.render(context,request))

def store(request): ## Not done - Just copied from index
    book_list= BookDetails.objects.order_by('-title')
    template=loader.get_template('book-store/store.html')
    context={'book_list0':book_list[0],
    'book_list1':book_list[1],
    'book_list2':book_list[2],
    'book_list3':book_list[3],
    'book_list4':book_list[4],
    'book_list5':book_list[5],
    'book_list6':book_list[6],
    'book_list7':book_list[7],
    'book_list8':book_list[8],
    'book_list9':book_list[9],
    'book_list10':book_list[10],
    'book_list11':book_list[11],
    }
    #print ("Context= ", context)
    return HttpResponse(template.render(context,request))


def bookDetails(request,id):
    book=BookDetails.objects.get(id=id)
    template=loader.get_template('book-store/bookDetails.html')
    context={'book':book,}
    return HttpResponse(template.render(context,request))





def signIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/book-store')
        else:
            messages.info(request,'Username or Password is incorrect')
            
    context={}
    return render(request,'book-store/signin.html',context)

	
	
def signUp(request):
    #form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Hello {username} !! Your account has been created successfully !!')
            return redirect("/book-store/signIn")
        else:
            print (form.errors)
    else:
        form=RegisterForm()
    return render(request,"book-store/signup.html",{"form":form})


def signOut(request):
    logout(request)
    return redirect("/book-store/signIn")

def myProfile(request):
    return render(request,'book-store/profile.html')

