from django.urls import path
from . import views

#App urls
urlpatterns = [
    path('', views.home, name="Home"),
    path('index', views.home, name="Home"),
    path('next', views.loadcontent, name="Loadcontent"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("actionUrl", views.storea_rticles,name="actionUrl"),







]

