from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"main/main.html",{'titleName': 'Ripplect', 'brandName':'Ripplect'})
