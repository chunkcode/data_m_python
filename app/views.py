from django.shortcuts import render,redirect,HttpResponse
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from app.pwd import getpass
from django.views.decorators.cache import never_cache

def landing(request):
 return render(request,'user/landing.html')

def logout_view(request):
 session_keys = list(request.session.keys())
 for key in session_keys:
   del request.session[key]
 print(session_keys)
 logout(request)
 return redirect('home')
@ratelimit(key='ip', rate='5/m',method='POST', block=True)
@never_cache
def login(request):
 if request.user.is_authenticated:
  return redirect('home')
 if request.method == 'POST':    
  username = request.POST.get('email')
  password = request.POST.get('password')
  user = authenticate(request,username=username,password=password)
  if user:
   auth_login(request,user)
   if user.is_staff:
    if user.is_superuser:
     return redirect('admin_dashboard')
    else:
     return redirect('manager_dashboard')     
   else:
     return redirect('home')
  messages.error(request,'Please provide valid credentials !')
  return render(request,'user/login.html')
 return render(request,'user/login.html')


@ratelimit(key='ip', rate='3/m', block=True)
@never_cache
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
 if request.user.is_staff:
  return render(request,'user/manager_dashboard.html')

@login_required(login_url='login')
def admin_dashboard(request):
 if request.user.is_superuser:
  return render(request,'user/admin_dashboard.html')

@login_required(login_url='login')
def admin_requested_accounts(request):
 if request.user.is_superuser:
  accounts = AccountRequest.objects.all()
  return render(request,'user/admin_requested_accounts.html',{'accounts':accounts})

@login_required(login_url='login')
def admin_accept_requested_account(request,id):
 if request.user.is_superuser:
  account = AccountRequest.objects.get(id= id)
  psw = getpass()
  print(psw)
  User.objects.create_user(  account.email,psw ,username = account.email ,name=account.name ,
       company = account.company ,mobile = account.phone,
       role = "user", subscribed = True, 
       )
  return render(request,'user/admin_accept_requested_account.html')