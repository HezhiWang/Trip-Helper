import os
import pandas as pd

def Read_data():
	"""
	This function Read_data read all four csv files: bookingNYC.csv, yelp_data.csv, museum.csv, attraction.csv, and
	return four dataframe as: data_hotel, data_restaurant, data_museum, data_attraction
	
	Exceptions:
		handle IOError exceptions
	"""
	try:
		path = os.getcwd() + '/Data/bookingNYC.csv'
		data_hotel = pd.read_csv(path, thousands = ',', encoding = 'latin1')

		path = os.getcwd() + '/Data/yelp_data.csv'
		data_restaurant = pd.read_csv(path, encoding = 'latin1')

		path = os.getcwd() + '/Data/museum.csv'
		data_museum = pd.read_csv(path, encoding = 'latin1')

		path = os.getcwd() + '/Data/attraction.csv'
		data_attraction = pd.read_csv(path, encoding = 'latin1')

		return data_hotel, data_restaurant, data_museum, data_attraction
	except IOError:
		print("Error: can\'t find file or read data")
	







































