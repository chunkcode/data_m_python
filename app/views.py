from django.shortcuts import render,redirect,HttpResponse
from django_ratelimit.decorators import ratelimit
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from app.pwd import getpass,add_pdf,add_ppt,add_excel,add_cat_icon
from django.views.decorators.cache import never_cache


def landing(request):
 return render(request,'user/landing.html')

def logout_view(request):
 session_keys = list(request.session.keys())
 for key in session_keys:
   del request.session[key]
 print(session_keys)
 logout(request)
 return redirect('landing')
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
 messages.error(request,"Access denied !")
 logout_view(request)
 return redirect('home')

@login_required(login_url='login')
def admin_dashboard(request):
 if request.user.is_superuser:
  return render(request,'user/admin_dashboard.html')
 messages.error(request,"Access denied !")
 logout_view(request)
 return redirect('home')

@login_required(login_url='login')
def admin_requested_accounts(request):
 if request.user.is_superuser:
  accounts = AccountRequest.objects.all()
  return render(request,'user/admin_requested_accounts.html',{'accounts':accounts})
 messages.error(request,"Access denied !")
 logout_view(request)
 return redirect('home')

@login_required(login_url='login')
def admin_accept_requested_account(request,id):
 if request.user.is_superuser:
  try:
   account = AccountRequest.objects.get(id= id)
   psw = getpass()
   print(psw)
   User.objects.create_user(  account.email,psw ,username = account.email ,name=account.name ,
       company = account.company ,mobile = account.phone,
       role = "user", subscribed = True, 
       )
   messages.error(request,"Account has been approved.")
   return redirect('admin_requested_accounts')
  except:
   messages.error(request,"Something went wrong !")
   return redirect('admin_requested_accounts')
 messages.error(request,"Access denied !")
 logout_view(request)
 return redirect('home')
 
@login_required(login_url='login')
def admin_reject_requested_account(request,id):
 if request.user.is_superuser:
  try:
   account = AccountRequest.objects.get(id= id)
   account.delete()
   messages.error(request,"Account has been rejected.")
   return redirect('admin_requested_accounts')
  except:
   messages.error(request,"Something went wrong !")
   return redirect('admin_requested_accounts')
 messages.error(request,"Access denied !")
 logout_view(request)
 return redirect('home')

def admin_report_type(request):
 if request.user.is_superuser:
  reports = ReportType.objects.all()

def admin_add_report_type(request):
 if request.user.is_superuser:
  try:
   if request.POST:
    type = ReportType()
    type.type = request.POST['report_type']
    type.save()
   return render(request,'admin/admin_add_report_type.html')
  except:
    messages.error(request,"Something went wrong !")
    return redirect('admin_requested_accounts')

def admin_edit_report_type(request,id):
 if request.POST:
  type = ReportType(id = id)
  type.type = request.POST['report_type']
  type.save()
 type = ReportType(id = id)
 context = {'report_type':type}
 return render(request,'admin/admin_edit_report_type.html',context=context)
 
def admin_add_cat(request):
 if request.POST:
  doc = request.FILES 
  icon = doc['icon']
  cat =Category()
  cat.name = request.POST['cat']
  cat.icon = ""
  cat.save()
  icon_name = add_cat_icon(icon,cat.id)
  cat.icon = icon_name
  cat.save()
 return render(request,'admin/admin_add_cat.html')

def admin_edit_cat(request,id):
 if request.POST:
  doc = request.FILES 
  cat = Category(id = id)
  if doc['icon']:
   icon = doc['icon']
   cat.icon = add_cat_icon(icon,cat.id)
  cat.name = request.POST['cat']
  cat.save()
 cat = Category(id = id)
 context = {'cat':cat}
 return render(request,'admin/admin_edit_cat.html',context=context)

def admin_add_sub_cat(request):
 if request.POST:
  doc = request.FILES 
  icon = doc['icon']
  sub =SubCategory()
  sub.name = request.POST['sub']
  sub.category = int(request.POST['sub'])
  sub.icon = ""
  sub.save()
  icon_name = add_cat_icon(icon,sub.id)
  sub.icon = icon_name
  sub.save()
  print("sub done")
 return render(request,'admin/admin_add_sub_cat.html')

def admin_edit_sub_cat(request,id):
 if request.POST:
  doc = request.FILES 
  sub =SubCategory(id = id)
  if doc['icon']:
   icon = doc['icon']
   sub.icon = add_cat_icon(icon,sub.id)
  sub.name = request.POST['sub']
  sub.category = int(request.POST['sub'])
  sub.save()
  print("sub done")
 sub_cat = SubCategory(id = id)
 context = {'sub_cat':sub_cat}
 return render(request,'admin/admin_edit_sub_cat.html',context=context)

def admin_add_report(request):
 if request.POST:
  doc = request.FILES
  report = Report() 
  if doc['pdf']: 
   pdf = doc['pdf']
   report.pdf = add_pdf(pdf,12)
  if request.FILES['power']:
   ppt = request.FILES['power']
   report.ppt = add_ppt(ppt,12)
  if doc['excel']:
   excel = doc['excel']
   report.excel = add_excel(excel,12)
  report.title = request.POST['title']
  report.detail = request.POST['detail']
  report.report_type = request.POST['report_type']
  report.category = request.POST['cat']
  report.subcategory = request.POST['sub']
  report.publish_date = request.POST['pub_date']
 return render(request,'admin/admin_add_report.html')

def admin_edit_report(request,id):
 if request.POST:
  doc = request.FILES
  report = Report.objects.get(id = id)
  if doc['pdf']: 
   pdf = doc['pdf']
   report.pdf = add_pdf(pdf,12)
  if request.FILES['power']:
   ppt = request.FILES['power']
   report.ppt = add_ppt(ppt,12)
  if doc['excel']:
   excel = doc['excel']
   report.excel = add_excel(excel,12)
  report.title = request.POST['title']
  report.detail = request.POST['detail']
  report.report_type = request.POST['report_type']
  report.category = request.POST['cat']
  report.subcategory = request.POST['sub']
  report.publish_date = request.POST['pub_date']
  print("DONE")
 report = Report(id = id)
 context = {'report':report}
 return render(request,'admin/admin_edit_report.html',context=context)


from django.http import FileResponse

def send_file(response):

    img = open('media\ppt\pdf_12.pptx', 'rb')

    response = FileResponse(img)
    response['Content-Disposition'] = 'attachment; filename="somefilename.pptx"'
    return response