'''
This module is a webscraper that gets information of restaurants in NYC from yelp.com.
It uses urllib to open urls and read the source html , and beautifulsoup to extract information,
including name, address, scores, reviews and latitudes & longitudes.
Every time when you implement this code, there will have some random advertisements and I have to handle them differently at each time.
This code doesn't include the above part but I handeled this every time I implement this code. 
Besides that, to get more data from yelp.com, I need to change the base website every time I implement this code. 
'''
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

restaurant_name = []
number_of_review = []
score_of_review = []
address = []
number_of_price = []
category = []
latitude = []
longitude = []

for i in range(50):
    a = str(i * 10)
    url1 = "https://www.yelp.com/search?find_loc=New+York,+NY"
    url2 = "&start=" + a
    url3 = "&cflt=restaurants"
    url = url1 + url2 + url3
    ht = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(ht, "lxml")

    #find restaurant name
    for t in soup.find_all('a', class_ = 'biz-name'):
        restaurant_name.append(t.text.replace(" ", "").strip())

    #find number of reviews of restaurant
    for t in soup.find_all('span', class_ = 'review-count'):
        number_of_review.append(t.text.strip().split(" ")[0])

    #find score of review of restaurant
    for t in soup.find_all('div', class_ = 'i-stars'):
        score_of_review.append(t.get('title').split(" ")[0].strip())

    #find address 
    for t in soup.find_all('address'):
        address.append(t.text.strip())

    #find number of price of restaurant
    for t in soup.find_all('span', class_ = 'business-attribute'):
        number_of_price.append(len(t.text))

    #find category of restaurant
    for t in soup.find_all('span', class_ = 'category-str-list'):
        category.append(t.text.replace(" ", "").replace("\n", "").strip())

    #find latitude and longitude of restaurant
    for t0 in soup.find_all('a', class_ = 'biz-name js-analytics-click'):
        base0 = 'https://www.yelp.com'
        hurl = base0 + t0.get('href',None)
        htre = urllib.request.urlopen(hurl).read()
        soup1 = BeautifulSoup(htre, "lxml")

        for t in soup1.find_all('div', class_ = 'lightbox-map hidden'):
            text = t.get('data-map-state').strip()
            index_lat = text.find('latitude') + 11
            index_lng = text.find('longitude') + 12
            latitude.append(text[index_lat:index_lat+9])
            longitude.append(text[index_lng: index_lng+10])

    #bulid a dictionary
    d = {'Name': restaurant_name, 'Address': address, 'category': category, 'Lat': latitude, 'Lng': longitude, \
        'number_of_price': number_of_price, 'Total_review': number_of_review, 'Avgscore': score_of_review}

    #save this dataframe as a csv file
    yelp_data = pd.DataFrame(d)
    yelp_data.to_csv('yelp_data.csv')




    
