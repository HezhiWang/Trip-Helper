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

	recommented_attraction = travel_data.iloc[:total_num_attractions, :]

	cordinate_data = []

	for i in range(recommented_attraction.shape[0]):
		temp = []
		temp.append(recommented_attraction['lat'].iloc[i])
		temp.append(recommented_attraction['lng'].iloc[i])
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

	recommented_center = center_points[recommendation_order, :]

	f = open('myfile','w')

	for i, item in enumerate(recommented_center):
		hotel_sorted = sort_within(hotel, item[0], item[1], 2, 'Price', bugdet_list)[:2]
		#restaurant_sorted = sort_within(restaurant, item[0], item[1], 3, 'ctg', bugdet)[:3]//////////////////////////////

		f.write('Day '+ str(i+1) + '\n')
		f.write('Attractions: ' + '\n')
		for x in index_list[recommendation_order[i]]:
			f.write(recommented_attraction.iloc[x]['name'] + '\n')
			f.write(recommented_attraction.iloc[x]['address'] + '\n')
			f.write(recommented_attraction.iloc[x]['description'] + '\n')
			f.write(recommented_attraction.iloc[x]['detail'] + '\n\n')

	
	f.close()







	"""
	for t in range(time):
		#index_list.append(labels[labels == i].tolist())
		f.write('Day '+ str(t) + '\n')
		f.write('Attractions: ' + '\n')
		for x in index_list[t]:
			f.write(recommented_attraction.iloc[x]['name'] + '\n')
			f.write(recommented_attraction.iloc[x]['address'] + '\n')
			f.write(recommented_attraction.iloc[x]['description'] + '\n')
			f.write(recommented_attraction.iloc[x]['detail'] + '\n\n')
		f.write('Restaurants: ' + '\n')
		for i in range(2):
			f.write(restaurant_sorted.iloc[i]['Name'] + '\n')			
			f.write(restaurant_sorted.iloc[i]['Address'] + '\n')
			f.write(restaurant_sorted.iloc[i]['Avgscore'] + '\n')
		f.write('Hotels: ' + '\n')
		for i in range(3):
			f.write(hotel_sorted.iloc[i]['Name'] + '\n')			
			f.write(hotel_sorted.iloc[i]['Address'] + '\n')
			f.write(hotel_sorted.iloc[i]['Avgscore'] + '\n')
	f.close()

	"""















