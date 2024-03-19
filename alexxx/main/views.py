from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main1.html')


def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName', 'Hello this is your Cookies', max_age=None)
    return html


def set_cookie(request):
    html = HttpResponse("<h1>Мой сайт</h1>")
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    html.set_cookie('visit_count', str(visit_count))
    return html


def delete_coc(request):
    html = HttpResponse('<h1>coc del</h>')
    html.delete_cookie('visit_count')
    return html
