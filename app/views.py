from django.shortcuts import render

# Create your views here.
def landing(request):
    
    return render(request,'user/DataM.html')

def login(request):
    
    return render(request,'user/DataM.html')

def register(request):
    
    return render(request,'user/DataM2.html')

def home(request):
    
    return render(request,'user/DataM.html')