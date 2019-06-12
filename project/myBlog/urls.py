from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    path('',views.blank),
    path('index/',views.index),
    path('index/id=<int:num>/',views.index),
    path('sendartical/',views.sendartical),
    path('browseartical/',views.browseartical),
    path('login/',views.login),
    path('loginsuccess/',views.loginsuccess),#一荒废
    path('quitlogin/',views.quitlogin),
    path('complete/',views.complete),
    path('verifycode/',views.verifycode),
    path('codetext/',views.codetext),

    path('upimg/',views.upimg),
    path('upimgsuccess/',views.upimgsuccess),
    path('call/',views.call),

]
