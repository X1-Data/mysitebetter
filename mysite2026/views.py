from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,JsonResponse,FileResponse
from django.shortcuts import render
from django.utils import datastructures
from . import views

def home(request):
    return HttpResponse("Hello from home.")

def info(request):
    data = {}
    print("request.META")
    for k,v in request.META.items():
        data[k] = v
        print("{k} : {v}")
    return JsonResponse(data)

def shopping(request):
    return render(request, "shopping.html")

def DSSI(request):
    file_path =r'E:\GIthub\mysite2026\mysite2026\DSSI.pdf'
    return FileResponse(open(file_path, 'rb'),
       content_type='application/pdf',
       as_attachment=False,
       filename='DSSI.pdf')
    
    