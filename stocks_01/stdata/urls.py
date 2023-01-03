from django.urls import path
from . import views

urlpatterns = [
    # pk_af52d225f7594757880cec88d7325ebe - public key
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('search.html', views.searchStock, name="search"),

]