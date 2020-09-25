from django.contrib import admin
from django.urls import path
from tcapi import views

from .views import PageView

urlpatterns = [
    path('', PageView.as_view(template_name="index.html")),
    path('missing/', PageView.as_view(template_name="missing.html")),
    #url(r'^api/tutorials$', views.tcapi),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tcapi),
    #url(r'^api/tutorials/published$', views.tcapi)
    path('<str:template>', PageView.as_view()),
]

