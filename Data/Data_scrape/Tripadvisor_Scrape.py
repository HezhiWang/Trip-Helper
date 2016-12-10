'''
This is a web scraper that gets data from tripadvisor.com.
We focus on webpages on NYC museums and attractions using urllib and beautifulsoup.
The scraper for museum and attraction are alomost the same with only minor changes
in url. We extract information for their names, addresses, ratings, number of reviews
and descriptions and save these to csv file
'''

import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd

#for NYC museums
base = "https://www.tripadvisor.com/Attractions-g60763-Activities-c49-New_York_City_New_York.html#ATTRACTION_LIST"
#for NYC attractions
#base = "https://www.tripadvisor.com/Attractions-g60763-Activities-c47-New_York_City_New_York.html#ATTRACTION_LIST"

base1 = "http://www.tripadvisor.com"
namelist =[]
addrlist =[]
reviewlist = []
ratinglist =[]
descriptionlist = []
time_feelist = []
lnglist = []
latlist = []
# page number
for i in range(0,9):
    a = str(i * 30)
    url1 = "https://www.tripadvisor.com/Attractions-g60763-Activities-c49"
    # for attractions:
    # url1 = "https://www.tripadvisor.com/Attractions-g60763-Activities-c47"
    url2 = "-New_York_City_New_York.html#ATTRACTION_LIST"
    url3 = "-oa" + a
    url = url1 + url3 + url2
    ht = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(ht,'lxml')

#find museum url
    for t in soup.find_all('div',class_ = 'property_title'):
        murl = base1 + t.a.get('href')
        mht = urllib.request.urlopen(murl).read()
        msoup = BeautifulSoup(mht, "lxml")
        
        #find museum name
        for t in msoup.find_all('h1',class_='heading_name'):
            name = t.text.strip()
            namelist.append(name)
            print(name)

        #find address & lat & lng
        for t in msoup.find_all('span',class_='format_address'):
            address = t.text.strip()[9:]
            addrlist.append(address)
            print(address)
        latlng = msoup.find_all('div',class_='mapContainer')
        if latlng:
            for t in latlng:
                lng = t.get('data-lng').strip()
                lat = t.get('data-lat').strip()   
        else:
            lng = -999
            lat = -999
        lnglist.append(lng)
        latlist.append(lat)
        print('lat',lat,'lng',lng)
        
        #find number of reviews
        reviews = msoup.find_all('span',class_='rate sprite-rating_rr rating_rr') 
        if reviews:
            for t in reviews:
                totalreview = t.img.get('content').strip()
                totalreview = int(float(totalreview))
        else:
            totalreview = -999
        reviewlist.append(totalreview)    
        print('reviews:',totalreview)
              
        #find visitor rating 
        
        ratings = msoup.find_all('a',class_ ='more') 
        if ratings:
            for t in ratings:
                rating = t.get('content')
                if rating:
                    print(rating.strip())
        else:
            rating = '-999'
            print('rating:',rating)
        ratinglist.append(rating)
        #find recommendation length of visit and fee
        details = msoup.find_all('div', class_='detail_section details')
        if details:
            dets=[]
            for t in details:
                if t.div:
                    detail = t.div.text.strip().replace('\n'," ")
                    dets.append(detail)
            if len(dets)>1:
                time_fee = dets[0].strip()
                if time_fee[-1]==':':
                        time_fee = time_fee+' <1 hour'
                try:
                    description = dets[-1].split('...')[1].strip()
                    description = re.sub('read more','',description)
                except:
                    description = dets[-1].strip()
                    description = re.sub('read more','',description)
            else:
                if dets[0][0]=='R':
                    time_fee = dets[0].strip()
                    if time_fee[-1]==':':
                        time_fee = time_fee+' <1 hour'
                    description = '-999'
                else:
                    time_fee = '-999'
                    try:
                        description = dets[0].split('...')[1].strip()
                        description = re.sub('read more','',description)
                    except:
                        description = dets[-1].strip()
                        description = re.sub('read more','',description)
        else:
            time_fee = '-999'
            description = '-999'
        time_feelist.append(time_fee)
        descriptionlist.append(description)
        print(time_fee)
        print(description)

d = {'name':namelist,'address':addrlist,'lat':latlist, 'lng':lnglist, 'rating':ratinglist, 'detail':time_feelist,'total_review':reviewlist,'description':descriptionlist} 
museum = pd.DataFrame(d)
museum.to_csv('museum.csv',encoding='utf-8')

