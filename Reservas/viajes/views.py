from django.shortcuts import render

# Create your views here.
from .models import Destino
from django.http import HttpResponse

def home_view(request):
    return render(request, "viajes/home.html")

def list_view(request):
    return render(request, "viajes/list.html")
    
def search_view(request, destino):
    return HttpResponse(f"tu destino es: {destino}")




