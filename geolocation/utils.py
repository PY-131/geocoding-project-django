import os
import requests as rqs
from dotenv import dotenv_values
from datetime import datetime

ENV = dotenv_values()  
def get_coordinates(address):
    """
    Queries Location API and get's coordinates
    """

    data = {
      'key': os.getenv('PRIVATE_TOKEN'),
      'q': address,
      'format': 'json'
      }
    try:
       response = rqs.get(os.getenv('URL'), params=data)
    except Exception as e:
       raise e

    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    res = {'lat': lat, 'lon': lon, 'address': address}
    return res


def get_iss_location():

    """ 
    this is a helper function that gets the location of the ISS (lat, lon)
    returns a dict
    """
    
    res = {}
    response = __run_request(os.getenv('ISS_URL'), "iss-now.json")

    if response['message'] == 'success':
      iss_pos = response['iss_position']
      res['lat'] = iss_pos['latitude']
      res['lon'] = iss_pos['longitude']
      # possibly reverse geocode for address
      #res['location']
    else:
      res['location'] = 'over water'
    return res 

def get_iss_people(): 

    """ 
    this is a helper function that gets the occupants of the ISS
    returns a dict
    """

    people = {}
    response = __run_request(os.getenv('ISS_URL'), "astros.json") 

    if response['message'] == 'success': 
      people['people'] = [person["name"] for person in response["people"]] 
    
    return people

def get_time_now(): return datetime.now()

def __run_request(url, endpoint):

    """

    helper runs request using requests library
    """

    URL = os.path.join(url, endpoint)

    res = {}
    try:
       response = rqs.get(URL).json()

    except Exception as e:
       raise e

    return response

