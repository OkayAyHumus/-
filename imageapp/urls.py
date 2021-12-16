from django.urls import path
from .views import imagefunction

urlpatterns = [
    path('', imagefunction)
]
  
