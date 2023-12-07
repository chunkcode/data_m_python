from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
def landing(request):
 return render(request,'user/landing.html')

@ratelimit(key='ip', rate='5/m',method='POST', block=True)
def login(request):
 if request.method == 'POST':    
  username = request.POST.get('email')
  password = request.POST.get('password')
  user = authenticate(request,username=username,password=password)
  if user:
   auth_login(request,user)
   if user.is_staff:
    if user.is_superuser:
     return redirect('manager_dashboard')
    else:
     return redirect('manager_dashboard')     
   elif user.role == "user":
     return redirect('home')
       
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

def forgot_password(request):
 if request.POST:
  email = request.POST['email'].strip()
  import smtplib    
  sender_mail = 'sender@fromdomain.com'        
  message = """From: From Person %s  
               To: To Person %s  
               MIME-Version:1.0  
               Content-type:text/html  
               Subject: Sending SMTP e-mail   
               <h3>Python SMTP</h3>  
               <strong>This is a test e-mail message.</strong>  
               """%(sender_mail,email)    
  try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, email, message)    
   print("Successfully sent email")    
  except Exception:    
   print("Error: unable to send email")    
 return render(request,'user/forgot_password.html')

@login_required(login_url='login')
def home(request):
    
    return render(request,'user/home.html')


@login_required(login_url='login')
def manager_dashboard(request):
    
    return render(request,'user/manager_dashboard.html')

@login_required(login_url='login')
def admin_dashboard(request):
    
    return render(request,'user/admin_dashboard.html')