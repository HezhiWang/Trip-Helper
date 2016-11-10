import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

for i in range(3):
    a = str(i * 10)
    url1 = "https://www.yelp.com/search?find_loc=New+York,+NY"
    url2 = "&start=" + a
    url3 = "&cflt=restaurants"
    url = url1 + url2 + url3
    restaurant_name = []
    number_of_review = []
    score_of_review = []
    address = []
    number_of_price = []
    category = []
    ht = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(ht, "lxml")
    
    for t in soup.find_all('a', class_ = 'biz-name'):
        restaurant_name.append(t.text.replace(" ", "").strip())#
    for t in soup.find_all('span', class_ = 'review-count'):
        number_of_review.append(t.text.strip().split(" ")[0])
    for t in soup.find_all('div', class_ = 'i-stars'):
        score_of_review.append(t.get('title').split(" ")[0].strip())
    for t in soup.find_all('address'):
        address.append(t.text.strip())#
    for t in soup.find_all('span', class_ = 'business-attribute'):
        number_of_price.append(len(t.text))#
    for t in soup.find_all('span', class_ = 'category-str-list'):
        category.append(t.text.replace(" ", "").replace("\n", "").strip())
    """
    for t in soup.find_all('a', class_ = 'biz-name'):
        rurl = "http://www.yelp.com" + t.get("href")
        ht1 = urllib.request.urlopen(rurl).read()
        soup1 = BeautifulSoup(ht1, "lxml")
        for t in soup1.find_all('div', class_ = 'lightbox-map'):
            num = t.get('data-map-state').find('latitude')
            print(t.get('data-map-state')[num+11:num+20])
    """

    