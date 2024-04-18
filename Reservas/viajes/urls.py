from django.urls import path
from . import views
from .views import home_view, list_view, search_view



urlpatterns = [
    path("",home_view),
    path('viajes/', list_view),
    # Define URLs para crear_modelo2 y crear_modelo3
    path('buscar/', search_view),
   
]