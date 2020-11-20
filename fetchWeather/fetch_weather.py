from requests import get
import json
from pprint import pprint
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/18560234'
weather = get(url).json()['items']
pprint(weather)
