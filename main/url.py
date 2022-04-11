from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("vote/", views.vote, name="vote"),
    path("button1/", views.button1, name="button1"),
    path("button2/", views.button2, name="button2"),
    path("result/", views.result, name="result")
]