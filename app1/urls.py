from django.urls import path
from .views import inicio, resultado

urlpatterns = [
    path('', inicio, name="inicio"),
    path('resultado/', resultado, name="resultado"),
]