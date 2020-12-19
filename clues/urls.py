from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
import clues.views as cViews

urlpatterns = [
    url(r'^$', cViews.index, name='index'),
    path('<str:page>', cViews.landing),
    path('thanks', cViews.landing),
    ]
