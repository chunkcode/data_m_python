from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

    
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True,unique=True)
    username = models.CharField(max_length=250,unique=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=250)
    mobile = models.CharField(max_length=100)
    subscribed = models.BooleanField(default=False)
    role = models.CharField(max_length=100, default='user')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    company =  models.CharField(max_length=250)
    account_created = models.DateField(auto_now_add=True)
    toBereset = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.name

class Plan(models.Model):
    id = models.AutoField(primary_key=True) 
    plan_name = models.CharField(max_length=250)
    validity_days = models.IntegerField()  
    def __str__(self):
        return self.plan_name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name
    
class ReportType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=250)
    def __str__(self):
        return self.type
        
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    detail = models.TextField(null=True)
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    publish_date = models.DateField(null=True)
    pdf =  models.CharField(max_length=250,null=True)
    ppt = models.CharField(max_length=250,null=True)
    excel = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.title
    
class News(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    detail = models.TextField()
    def __str__(self):
        return self.title
    
class Access(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    started_date = models.DateField()
    validity_date = models.DateField()
    
class AccountRequest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    company =  models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    requested_date = models.DateField(auto_now_add=True)

class PlanRequest(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_date = models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

class ReportRequest(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_date = models.DateField(auto_now_add=True)
    message = models.TextField()

class Otp(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.TextField()
    otp = models.IntegerField()

class DownloadData(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
