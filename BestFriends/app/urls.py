from django.urls import path
from django.conf.urls import url

from . import views
app_name = 'app'
urlpatterns = [path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),

    url(r'',views.error404,name='404error')]