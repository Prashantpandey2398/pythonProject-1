from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def login(request):
    return render(request, 'index.html', context=None)

def naman(request):
    return render(request, 'Naman.html', context=None)

def hitesh(request):
    return render(request, 'Hitesh.html', context=None)

def nishit(request):
    return render(request, 'Nishit.html', context=None)

def abhya(request):
    return render(request, 'Abhya.html', context=None)

def agrima(request):
    return render(request, 'Agrima.html', context=None)

def piyush(request):
    return render(request, 'Piyush.html', context=None)

def praman(request):
    return render(request, 'Naman.html', context=None)

def prashant(request):
    return render(request, 'Prashant.html', context=None)

def shivani(request):
    return render(request, 'Shivani.html', context=None)

def channel(request):
    return render(request, 'channel.html', context=None)

def home(request):
    context = {
        'n': range(10),
    }
    return render(request, 'home.html', context)

def videoviewing(request):
    return render(request, 'Video Viewing.html', context=None)

def about(request):
    return None