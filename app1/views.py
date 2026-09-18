from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def vista1_app1(request):
    return render(request, 'app1/vista1_app1.html')

def vista2_app1(request):
    return render(request, 'app1/vista2_app1.html')