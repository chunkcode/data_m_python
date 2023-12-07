from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
def landing(request):
    
    return render(request,'user/landing.html')

@ratelimit(key='ip', rate='5/m',method='POST', block=True)
def login(request):
    
    return render(request,'user/login.html')

@ratelimit(key='ip', rate='3/m', block=True)
def register(request):
    if request.POST:
     name =  request.POST['name']
     email =  request.POST['email']
     company =  request.POST['company']
     phone =  request.POST['phone']
     AccountRequest(name =name, email=email,company=company,phone=phone).save()
     messages.error(request,"Registered Sucessfully!\nOur Team will contact you soon.")
     return render(request,'user/register.html')
    return render(request,'user/register.html')



@login_required(login_url='login')
def home(request):
    
    return render(request,'user/DataM.html')
