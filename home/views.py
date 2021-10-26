from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsModel
from .models import AppModel

# Create your views here.

def index(request):
    newsdata=NewsModel.objects.raw('select * from home_NewsModel order by id desc' )
    appdata=AppModel.objects.raw('select * from home_AppModel order by id desc')
    params={
        'newsdata':newsdata,
        'appdata':appdata,
    }
    return render(request,'home/index.html',params)

def aboutus(request):
    return render(request,'home/aboutUs.html')