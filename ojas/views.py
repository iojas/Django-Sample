from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return render(req, 'personal/home.html')

# Create your views here.
