import os
import pandas as pd

def Read_data():
	path = os.getcwd() + '/Data/bookingNYC.csv'
	data_hotel = pd.read_csv(path, thousands = ',', encoding = 'latin1')

	path = os.getcwd() + '/Data/yelp_data.csv'
	data_restaurant = pd.read_csv(path, encoding = 'latin1')

	path = os.getcwd() + '/Data/museum.csv'
	data_museum = pd.read_csv(path, encoding = 'latin1')

	path = os.getcwd() + '/Data/attraction.csv'
	data_attraction = pd.read_csv(path, encoding = 'latin1')

	return data_hotel, data_restaurant, data_museum, data_attraction







































