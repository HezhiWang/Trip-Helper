# Google geo-coding API 

# Input: formatted street address

import urllib
import json
import requests
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

for add in f:
    address = add.rstrip()
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    try:
        data = requests.get(url).json()
    except: 
        data = None
    if 'status' not in data or data['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)