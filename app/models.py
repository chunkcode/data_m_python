from django.db import models


class Plan(models.Model):
    plan_name = models.CharField(max_length=250)
    validity_days = models.IntegerField()
    
class User(models.Model):
    username = models.CharField(max_length=250,primary_key=True,unique=True)
    email = models.CharField(max_length=250,unique=True)
    password = models.CharField(max_length=250)
    mobile = models.CharField(max_length=100)
    subscribed = models.BooleanField(default=False)
    role = models.CharField(max_length=100, default='user')
    company =  models.CharField(max_length=250)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    icon = models.CharField(max_length=250)
    
class SubCategory(models.Model):
    name = models.CharField(max_length=250,unique=True)
    icon = models.CharField(max_length=250)

class ReportType(models.Model):
    type = models.CharField(max_length=250)
    
class Report(models.Model):
    title = models.TextField()
    detail = models.TextField()
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    pdf =  models.CharField(max_length=250)
    ppt = models.CharField(max_length=250)
    excel = models.CharField(max_length=250)

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField()
    detail = models.TextField()
    
class Access(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    started_date = models.DateField()
    validity_date = models.DateField()
    
    