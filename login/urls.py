from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.auth, name='auth')
]

