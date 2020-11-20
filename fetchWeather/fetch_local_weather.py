from requests import get
import json
from pprint import pprint
from haversine import haversine


stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
my_lat = 7.888540
my_lon = 47.705170
all_stations = get(stations).json()['items']
def find_closest():
    smallest = 56689
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()

weather = weather + str(closest_stn)

my_weather = get(weather).json()['items']
pprint(list(my_weather))

