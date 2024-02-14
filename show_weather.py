#!/usr/bin/python

import json
import requests
import sys


# Service: Weather API
# URL: https://www.weatherapi.com/
# Account: gkusumoto+weatherapi@gmail.com
# Password: kud****o
# API Key: 1e4805948bb54c4782021001241402


#https://api.weatherapi.com/v1/current.json?key=1e4805948bb54c4782021001241402&q=Tokyo&aqi=yes
API_HOST = 'api.weatherapi.com'
API_KEY = '1e4805948bb54c4782021001241402'
URL = f"https://{API_HOST}/v1/current.json?key={API_KEY}&q=Tokyo"

try:
	response = requests.get(URL)
	#print(response.text)
except Exception as e:
	print(e)
	sys.exit(1)

weather = json.loads(response.text)
print(json.dumps(weather, indent=4))
