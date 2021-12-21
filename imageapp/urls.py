from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   
    path('', views.classify, name="classify")
    path('login/', views.classify, name="classify")
]
  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
