from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def rooms(request):
    context = {}
    return render(request, 'base/rooms.html', context)