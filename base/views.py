from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)

def rooms(request):
    context = {}
    return render(request, 'rooms.html', context)