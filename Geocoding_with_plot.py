# Google geo-coding API 

# Input: formatted street address

file = '../desktop/addr.txt'  # address book for test
f = open(file)
f = f.readlines()

import urllib
import json
import requests
import codecs
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

fhand = codecs.open('where.js','w', "utf-8")
fhand.write("myData = [\n")
count = 0

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
    where = data['results'][0]['formatted_address']
    try:
        print('lat',lat,'lng',lng,'addr',where)
        count += 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
fhand.close()