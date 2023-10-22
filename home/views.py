from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    
    dataRequest = requests.get('https://fakestoreapi.com/products/category/jewelery', params=request.GET)
    if dataRequest.status_code == 200:
        return render(request,"index.html",{'Products': dataRequest.json()})
    else:
        return HttpResponse("Something went wrong, please try again later")