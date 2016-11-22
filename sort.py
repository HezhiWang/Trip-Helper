import urllib
import json
import requests
import pandas as pd
import codecs
from geopy.distance import vincenty

def distance(lat1,lng1,lat2,lng2):
    add1 = (lat1,lng1)
    add2 = (lat2,lng2)
    d = vincenty(add1, add2).miles
    return d

def sort_within(df, centerlat, centerlng, distance_within, given_filter, value):
	'''
	find index of locations in dataframe df that's within a given distance of a given center 
	and have with the given value of the given filter, and then sort by score and total reviews
	'''
	ind = []
	for i in range(0,df.shape[0]):
		lat = df['lat'].ix[i]
		lng = df['lng'].ix[i]
		if distance(lat,lng,centerlat,centerlng) <= distance_within:
			ind.append(i)
	df_within = df.ix[ind]
	df_sub = df_within[df_within[given_filter]==value]
	df_sorted = df_sub.sort_values(by = ['avgscore','total_review'],ascending=[False, False])
	return df_sorted
'''
data = pd.read_csv('bookingQueens.csv',thousands=',')
data = data.drop_duplicates(subset=['name','address'], keep='first')
df = sort_within(data,40.748817, -73.985428, 100, 'price', 3)
print(df)
'''

