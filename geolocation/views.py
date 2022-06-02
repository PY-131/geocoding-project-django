from django.shortcuts import render
from django.http import JsonResponse
from .forms import AddressForm
from .utils import *

def index(request):
    
    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            addy = form.cleaned_data['address']
            res = get_coordinates(addy)
            return render(request, 'geolocation/results.html', res)
    else:
    	form = AddressForm()
    return render(request, 'geolocation/index.html', {'form': form})

def iss_people(request):
	return JsonResponse(get_iss_people())

def iss_location(request):
	return JsonResponse(get_iss_location())

def iss_info(request):
	
	people = get_iss_people()
	location = get_iss_location()
	people.update(location)
	return JsonResponse(people)


def get_time(request):

    time_now = get_time_now()
    return JsonResponse(time_now)



