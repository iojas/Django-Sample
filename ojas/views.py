from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(req):
    resp = requests.get('http://www.omdbapi.com/?s=harry potter')

    for x in resp.json()['Search']:
        for k,v in x.iteritems():
            print k+ " " +v



    return render(req, 'personal/home.html',{'movies':resp.json()['Search']})


# Create your views here.
