import pandas as pd
from geopy.distance import vincenty

def distance(lat1, lng1, lat2, lng2):
	'''
	Calculate the distance (miles) between 2 locations given their latitudes and longitudes
	'''
    add1 = (lat1,lng1)
    add2 = (lat2,lng2)
    d = vincenty(add1, add2).miles
    return d

def sort_within(df, centerlat, centerlng, distance_within, given_filter = None, value = None):
	'''
	Find index of locations in dataframe that's within a distance from a center, 
	and then sort by score and total reviews both descending.
	if a filter is given, select a subset before sorting.

	Parameters:
	df: input dataframe of locations
	centerlat: latitude of the center
	centerlng: longitude of the center
	distance_within: the maximum distance from the center to a certain location
	given_filter: select a subset of the dataframe by the filter before sorting. If None, sort directly.
	value: select a subset of the dataframe satisfying "given_filter == value". If None, sort directly.

	'''
	ind = []
	for i in range(0,df.shape[0]):
		lat = df['Lat'].ix[i]
		lng = df['Lng'].ix[i]

		if distance(lat,lng,centerlat,centerlng) <= distance_within:
			ind.append(i)
	df_within = df.ix[ind]

	if (not given_filter):
		df_sub = df_within.sort_values(by = ['Avgscore','Total_review'], ascending=[False, False])
		df_sorted = df_sub[:3]	
		return df_sorted
	else:
		if (given_filter == 'Price'):
			df_sub = df_within[df_within[given_filter].isin(value)]
			df_sorted = df_sub.sort_values(by = ['Avgscore','Total_review'], ascending=[False, False])
		elif (given_filter == 'ctg'):
			df_within['Distance'] = df.apply(lambda x: distance(x['Lat'],x['Lng'],centerlat,centerlng), axis = 1)
			df_within['Reviews'] = df.apply(lambda x: review_transform(x['Total_review']), axis = 1)
			df_sub = df_within[df_within[given_filter]==value]
			df_sorted = df_sub.sort_values(by = ['Avgscore','Total_review'], ascending=[False, False])
		
		if (df_sorted.shape[0] > 10):
			df_sorted = df_sorted[:10]
	return df_sorted


def review_transform(num):
	'''
	Transform reviews(num) by range for plotting radar chart.
	'''
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

def sort_museums_or_attractions(df):
    '''
    for museums/attractions with ratings higher than 3.5 and total number of reviews 
    more than 1000, sort by rating and total reviews both descending.
    This is to generate search results for search museum/attraction part.
    '''
    mask1 = df['Avgscore']>=3.5
    mask2 = df['Total_review']>=1000
    mask = pd.concat((mask1, mask2), axis=1)
    ind_sub = mask.all(axis=1)
    df_sub = df.ix[ind_sub]
    df_sorted = df_sub.sort_values(by=['Avgscore','Total_review'],ascending=[False,False])
    return df_sorted


