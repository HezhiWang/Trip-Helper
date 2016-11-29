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

def review_transform(num):
	if (num >= 1000):
		return 5
	elif (700 <= num < 1000):
		return 4
	elif (400 <= num < 700):
		return 3
	elif (100 <= num < 400):
		return 2
	elif (num < 100):
		return 1

def sort_within(df, centerlat, centerlng, distance_within, given_filter, value):
	'''
	find index of locations in dataframe df that's within a given distance of a given center 
	and have with the given value of the given filter, and then sort by score and total reviews
	'''
	ind = []

	if (given_filter == 'ctg'):
			df['Distance'] = df.apply(lambda x: distance(x['Lat'],x['Lng'],centerlat,centerlng), axis = 1)
			df['Reviews'] = df.apply(lambda x: review_transform(x['number_of_review']), axis = 1)

	for i in range(0,df.shape[0]):
		lat = df['Lat'].ix[i]
		lng = df['Lng'].ix[i]

		if distance(lat,lng,centerlat,centerlng) <= distance_within:
			ind.append(i)
	df_within = df.ix[ind]

	if (given_filter == 'Price'):
		df_sub = df_within[df_within[given_filter].isin(value)]
		df_sorted = df_sub.sort_values(by = ['Avgscore','Total_review'], ascending=[False, False])
	if (given_filter == 'ctg'):
		df_sub = df_within[df_within[given_filter]==value]
		df_sorted = df_sub.sort_values(by = ['score_of_review','number_of_review'], ascending=[False, False])
		

	if (df_sorted.shape[0] > 10):
		df_sorted = df_sorted[:10]
	return df_sorted


