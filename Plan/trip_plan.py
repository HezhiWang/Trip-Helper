import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import os
from sklearn.cluster import KMeans
from Data.Read_data import *
from Sort.sort import *
from geopy.distance import vincenty

def distance(lat1,lng1,lat2,lng2):
    add1 = (lat1,lng1)
    add2 = (lat2,lng2)
    d = vincenty(add1, add2).miles
    return d

def revised_kmeans(index_list, order_list, cordinate_data, center_points, time, degree):
    for k, i in enumerate(order_list):
        if (degree == 1):
        	n = len(index_list[i]) - 2
        elif (degree == 2):
        	n = len(index_list[i]) - 4
        for x in range(n):
            #find max distance
            d = 0
            max_index = 0
            for index in range(len(index_list[i])):
                if (d < distance(cordinate_data[index][0], cordinate_data[index][1],center_points[i][0], center_points[i][1])):
                    d = distance(cordinate_data[index][0], cordinate_data[index][1],center_points[i][0], center_points[i][1])
                    max_index = index
            #calculate minimal distance to a cluster j, j != i
            d = 10000
            min_index = 0
            for index in order_list[k+1:]:
                if (d > distance(cordinate_data[max_index][0], cordinate_data[max_index][1],center_points[index][0], center_points[index][1])):
                    d = distance(cordinate_data[max_index][0], cordinate_data[max_index][1],center_points[index][0], center_points[index][1])
                    min_index = index
            #add
            index_list[min_index].append(index_list[i][max_index])
            #delete
            del index_list[i][max_index]
        #recalculate centroids    
        center_points = []
        for j in range(time):
            cordinate_subdata = [cordinate_data[h] for h in index_list[j]]
            kmeans = KMeans(n_clusters=1, random_state=0).fit(cordinate_subdata)
            center_points.append([kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1]])
    return index_list, center_points

def trip_planer(time, bugdet, degree):


	path = os.getcwd()
	travel_data = pd.read_csv(path + '/Data/trip_plan.csv', encoding = 'latin1') 
	#travel_data = travel_data[travel_data['lat'] != -999]
	df = df.replace(to_replace= '-999', value='N.A.')
	hotel, restaurant, museum, attraction = Read_data()


	if (degree == 1):
		total_num_attractions = time * 2
	elif (degree == 2):
		total_num_attractions = time * 4

	if (bugdet == 1):
		bugdet_list = [1,2]
	elif (bugdet == 2):
		bugdet_list = [3,4]
	elif (bugdet == 3):
		bugdet_list = [5]

	recommended_attraction = travel_data.iloc[:total_num_attractions, :]
	recommended_attraction = recommended_attraction.replace(to_replace= '-999', value='N.A.')

	cordinate_data = []

	for i in range(recommended_attraction.shape[0]):
		temp = []
		temp.append(recommended_attraction['lat'].iloc[i])
		temp.append(recommended_attraction['lng'].iloc[i])
		cordinate_data.append(temp)

	kmeans = KMeans(n_clusters = time, random_state = 0).fit(cordinate_data)
	
	a = pd.Series(kmeans.labels_)
	index_list = {}
	for i in range(time):
		index_list[i] = (a[a == i].index.tolist())
	order_list = sorted(index_list, key=lambda k: len(index_list[k]), reverse = True)

	center_points = kmeans.cluster_centers_

	index_list, center_points = revised_kmeans(index_list, order_list, cordinate_data, center_points, time, degree)

	center_points = np.asarray(center_points)
	recommendation_order = np.random.permutation(time)

	recommended_center = center_points[recommendation_order, :]

	f = open('Trip_Plan.rtf','w')
	f.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}}')

	for i, item in enumerate(recommended_center):
		hotel_sorted = sort_within(hotel, item[0], item[1], 2, 'Price', bugdet_list)
		recommended_hotel = hotel_sorted.reindex(np.random.permutation(hotel_sorted.index))[:2]

		restaurant_sorted = sort_within(restaurant, item[0], item[1], 3)
		recommended_restaurant = restaurant_sorted.reindex(np.random.permutation(restaurant_sorted.index))[:3]

		f.write(r'\qc \b Day{} \b0 \qc0 \line'.format(str(i+1)))
		f.write(r'\b Attractions: \b0 \line')
		for x in index_list[recommendation_order[i]]:
			f.write(r'{} \line'.format(recommended_attraction.iloc[x]['name']))
			f.write(r'Address: \enspace {} \line'.format(recommended_attraction.iloc[x]['address']))
			f.write(r'Description: \enspace {} \line'.format(recommended_attraction.iloc[x]['description']))
			f.write(r'Detail: \enspace {} \line \line'.format(recommended_attraction.iloc[x]['detail']))

		f.write(r'\b Hotel: \b0 \line')
		for x in range(2):
			f.write(r'{} \line'.format(recommended_hotel.iloc[x]['name']))
			f.write(r'Address: \enspace {} \line'.format(recommended_hotel.iloc[x]['address']))
			f.write(r'Score: \enspace {} \line \line'.format(recommended_hotel.iloc[x]['Avgscore']))
			f.write(r'Reviews: \enspace {} \line'.format(recommended_hotel.iloc[x]['Total_review']))

		f.write(r'\b Restaurant: \b0 \line')
		for x in range(3):
			f.write(r'{} \line'.format(recommended_restaurant.iloc[x]['name']))
			f.write(r'Address: \enspace {} \line'.format(recommended_restaurant.iloc[x]['address']))
			f.write(r'Score: \enspace {} \line'.format(recommended_restaurant.iloc[x]['Avgscore']))
			f.write(r'Reviews: \enspace {} \line'.format(recommended_restaurant.iloc[x]['Total_review']))
		f.write(r'\line \line')

	f.write(r'}\n\x00')
	f.close()















