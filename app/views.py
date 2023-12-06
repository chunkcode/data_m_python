from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from .models import *
def landing(request):
    
    return render(request,'user/DataM.html')

@ratelimit(key='ip', rate='5/m', block=True)
def login(request):
    
    return render(request,'user/DataM.html')

@ratelimit(key='ip', rate='5/m', block=True)
def register(request):
    if request.POST:
     name =  request.POST['name']
     email =  request.POST['email']
     password =  request.POST['password']
     company =  request.POST['company']
     phone =  request.POST['phone']
     AccountRequest(name =name, email=email,password=password,company=company,phone=phone).save()
     messages.error(request,"Registered Sucessfully!\nOur Team will contact you soon.")
     return render(request,'user/DataM2.html')
    return render(request,'user/DataM2.html')

def home(request):
    
    return render(request,'user/DataM.html')
