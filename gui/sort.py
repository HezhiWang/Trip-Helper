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
		lat = df['Lat'].ix[i]
		lng = df['Lng'].ix[i]
		if distance(lat,lng,centerlat,centerlng) <= distance_within:
			ind.append(i)
	df_within = df.ix[ind]
	df_sub = df_within[df_within[given_filter].isin(value)]
	df_sorted = df_sub.sort_values(by = ['Avgscore','Total_review'],ascending=[False, False])
	if (df_sorted.shape[0] > 10):
		df_sorted = df_sorted[:10]
	return df_sorted


