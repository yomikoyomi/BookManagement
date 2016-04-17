from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from info.models import trn_infomation

def index(request):
    if 'login_info' not in request.session:
        return HttpResponse('セッションないよ')

    infomation = trn_infomation.objects.all().order_by('id').reverse()
    return render(request, 'info/index.html',
    {'infomation': infomation})
#    return HttpResponse(request.session['login_info'])


