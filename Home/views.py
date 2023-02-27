from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserAddForm,ProductAddForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Product

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        
        user = authenticate(request, username = username,password = password )
        if user is not None:
            login(request,user)
            return redirect("Index")
        else:
            messages.info(request,"Username Or Password Incorrect")
            return redirect('SignIn')
        
        
    return render(request,'login.html')

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"User Created") 
            return redirect('Index')
        else:
            messages.info(request,"Form Is not valid") 
    context = {
        "form":form
    }
    return render(request,'register.html',context)

def Index(request):
    produ = Product.objects.all()
    context = {
        "produ":produ
    }
    return render(request,"Index.html",context)

def AddProduct(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.user = request.user
            product.save()
            messages.info(request,"Product Created")
            return redirect('AddProduct')
    context = {
        "form":form
    }
    return render(request,'addproduct.html',context)
