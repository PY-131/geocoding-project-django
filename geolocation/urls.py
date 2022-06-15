from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('iss_people', views.ISSPeople.as_view(), name='iss_people'),
    path('iss_location', views.ISSLocation.as_view(), name='iss_location'),
    path('iss_info', views.ISSInfo.as_view(), name='iss_info'),
    path('get_time', views.Time.as_view(), name='time_'),

]