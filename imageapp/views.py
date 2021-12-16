from django.shortcuts import render
# from django.http import HttpResponse

def imagefunction(request):
    return render(request, 'imageapp/hello.html')
