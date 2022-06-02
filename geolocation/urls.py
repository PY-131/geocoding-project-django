from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iss_people', views.iss_people, name='iss_people'),
    path('iss_location', views.iss_location, name='iss_location'),
    path('iss_info', views.iss_info, name='iss_info'),
    path('get_time', views.get_time, name='time_'),

]