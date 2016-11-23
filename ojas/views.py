from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

import requests

def index(req):
    if req.method == 'GET':
        resp = requests.get('http://www.omdbapi.com/?s=harry potter&type=movie')
        return render(req, 'personal/home.html', {'movies': resp.json()['Search']})

    if req.method == 'POST':

        mov = req.POST.get('conf')
        print mov
        if(mov):
            string = 'http://www.omdbapi.com/?s='+mov+'&type=movie'
            resp = requests.get(string)
            print resp
            if(resp.json()['Response']=='False'):
                return render(req, 'personal/home.html', {'movies': ''})
            else:
                return render(req, 'personal/home.html', {'movies': resp.json()['Search']})

        else:
            string = 'http://www.omdbapi.com/?s=spider&type=movie'
            resp = requests.get(string)
            return render(req, 'personal/home.html', {'movies': resp.json()['Search']})



