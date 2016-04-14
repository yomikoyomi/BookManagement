from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


def index(request):
    """ ログインセッションが存在した場合、infoへ飛ばす """
    if 'login_info' in request.session:
        return HttpResponseRedirect('/bookManagement/info/')

    return render(request, 'login/index.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        request.session.set_expiry(0)
        request.session['login_info'] = user.username
        return HttpResponseRedirect('/bookManagement/info/')
    else:
        return HttpResponse('ログイン失敗')
