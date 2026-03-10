from django.shortcuts import render
from .models import Granite

def home(request):
    granites = Granite.objects.all()
    return render(request, 'app1/home.html', {'granites': granites})

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')