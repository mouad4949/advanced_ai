from django.urls import path,include
from . import views


app_name = 'ai'

urlpatterns = [
    path("", views.index, name="index"),
    path("back/", views.BackOffice, name="baff"),
    path("login_back/", views.login_view_b, name="login_back"),
    path("login_front/", views.login_view_f, name="login_front"),
]