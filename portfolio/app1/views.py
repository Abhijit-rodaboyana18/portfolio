from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def personal(request):
    return render(request,'personal.html')

def skills(request):
    return render(request,'skills.html')

def experience(request):
    return render(request,'experience.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')