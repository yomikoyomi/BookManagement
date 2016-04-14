from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    """ TODO ログインセッションが存在した場合、infoへ飛ばす """
    return render(request, 'login/index.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse('ログイン成功')
    else:
        return HttpResponse('ログイン失敗')
