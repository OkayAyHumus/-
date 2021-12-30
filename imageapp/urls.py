from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
