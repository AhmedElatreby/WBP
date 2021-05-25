from django.shortcuts import render

def home(request):
    return render(request, 'navigation/home.html')

def options(request):
    return render(request, 'navigation/options.html')