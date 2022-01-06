from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imageapp.urls')),
]


# from imageapp import views

# handler500 = views.my_customized_server_error