from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    import requests
    import json

    api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=84b612b3bf4a4614a94d39a29eb99e3c")
    api = json.loads(api_request.content)
    
    return render(request,'index.html',{'data' : api})