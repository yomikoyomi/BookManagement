from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


def index(request):
    if 'login_info' not in request.session:
        return HttpResponse('セッションないよ')
    return HttpResponse(request.session['login_info'])
