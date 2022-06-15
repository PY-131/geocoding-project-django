from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .forms import AddressForm
from .utils import *

class Index(View):

    def get(self, request, *args, **kwargs):
        form = AddressForm()
        return render(request, 'geolocation/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            addy = form.cleaned_data['address']
            res = get_coordinates(addy)
            return render(request, 'geolocation/results.html', res)
        else:
            return render(request, 'geolocation/index.html', {'form': form})


class ISSPeople(View):

    def get(self, request, *args, **kwargs):

        return JsonResponse(get_iss_people())


class ISSLocation(View):

    def get(self, request, *args, **kwargs):
        
        return JsonResponse(get_iss_location())



class ISSInfo(View):

    def get(self, request, *args, **kwargs):
        people = get_iss_people()
        location = get_iss_location()
        people.update(location)
        return JsonResponse(people)


class Time(View):

    def get(self, request, *args, **kwargs):	
        time_now = get_time_now()
        res = {'time': time_now}
        return JsonResponse(res)

