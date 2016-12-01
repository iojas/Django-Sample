from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response

import requests

def index(req):
    if req.method == 'GET':
        if not req.session.has_key('username'):
            return redirect('/form/login')
        resp = requests.get('http://www.omdbapi.com/?s=spider&type=movie')
        return render(req, 'personal/home.html', {'movies': resp.json()['Search']})

    if req.method == 'POST':
        mov = req.POST.get('conf')
        y = req.POST.get('year')
        print mov
        if(mov):
            if(y):
                print 'year used '+y
                string = 'http://www.omdbapi.com/?s='+mov+'&type=movie&y='+y
            else:
                string = 'http://www.omdbapi.com/?s=' + mov + '&type=movie'
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

def shwoMovie(req):
    titleId = req.GET['i']
    resp = requests.get('http://www.omdbapi.com/?i='+titleId)
    print resp.json()['Title']
    return render(req, 'personal/movie.html', {'movie': resp.json()})



