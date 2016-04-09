from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ TODO ログインセッションが存在した場合、infoへ飛ばす """
    return render(request, 'login/index.html')


def auth(request):
    return HttpResponse('ログイン認証')
