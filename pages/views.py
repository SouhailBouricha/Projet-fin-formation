from django.shortcuts import render
from .models import Team
# Create your views here.

def home(request):
    Teams = Team.objects.all()
    data = {
        'teams': Teams,
    }
    return render(request,'pages/home.html',data)

def about(request):
    Teams = Team.objects.all()
    data = {
        'teams': Teams,
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')
    
def contact(request):
    return render(request,'pages/contact.html')
