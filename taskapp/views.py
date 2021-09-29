from django.contrib import auth
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from.forms import SignupForm,LoginForm,EditForm
from django.contrib.auth import logout

from .models import Signup


def home(request):
    return render (request,'home.html')

def login(request):
    form=LoginForm()
    print(form)
    return render(request,'login.html',{'form':form})

def signup(request):
    form=SignupForm()
    print(form)
    return render(request,'sign_up.html',{'form':form})

def userdetail(request):
    obj=Signup.objects.all()
    return render(request,'userdetail.html',{'user':obj})

def validation(request):
    try:
        errormsg=''
        if request.POST:
            form=SignupForm(request.POST)
            if request.POST['password']==request.POST['confirm']:
                if form.is_valid():  
                    form.save()
                    errormsg="Saved"
            else:
                errormsg="Password not Match"
            return render(request,'sign_up.html',{'errormsg':errormsg,'form':form})
    
    except Exception as e:
        print(e)
        return render(request,'sign_up.html',{'errormsg':"Error"})

def validlogin(request):
    try:
        
        form=LoginForm()
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            obj=Signup.objects.filter(email=email,password=password)
            print(obj)
            if obj.exists():
                obj=Signup.objects.filter(email=email)
                return render(request,'viewuser.html',{'user':obj})
            else:
                errormsg="invalid login"
                return render(request,'login.html',{'msg':errormsg,'form':form})
    except Exception as e:
        print(e)
        return HttpResponse("Error")
id=0
def alter(request):
    try:
        print("hello")
        if request.method=='POST' and "Edit"  in request.POST['action']:
            print(request.POST['action'])
            val=request.POST['action']
            global id
            id=int(val[4:])
            print(id)
            print(request.POST['name'])
            '''name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            print(name,email,address)'''
            obj=Signup.objects.filter(id=id)
            return render(request,'edit.html',{'user':obj})
        if request.method=='POST' and "Update" in request.POST['action']  :
            email=request.POST['email']
            name=request.POST['name']
            address=request.POST['address']
            obj1=Signup.objects.filter(id=id)
            print(obj1)
            print(email,id)
            obj=Signup.objects.filter(email=email,id=id).values()
            if obj.exists():
                Signup.objects.filter(id=id).update(address=address,username=name)
            elif Signup.objects.filter(email=email).exists()==False:
                 Signup.objects.filter(id=id).update(email=email,address=address,username=name)
            else:
                return render(request,'edit.html',{'user':obj1.values(),'msg':"Email in use"})
            obj=Signup.objects.all()
            return render(request,'userdetail.html',{'user':obj})
        if request.method=='POST' and "Delete"  in request.POST['action']:
            print(request.POST['action'])
            val=request.POST['action']
            id=int(val[6:])
            print(id)
            print(request.POST['name'])
            Signup.objects.filter(id=id).delete()
            obj=Signup.objects.all()
            return render(request,'userdetail.html',{'user':obj})
            
    except Exception as e:
        print(e)
        return render(request,'edit.html')
def logoutview(request):
    return render(request,'home.html')
       
            


# Create your views here.
