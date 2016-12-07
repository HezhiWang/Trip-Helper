from plot.draw import *
from Sort.sort import *
from Sort.yelp_sort import *
from plot.heatmap import *
import os
import sys
from Data.Read_data import *


class Page_creator:

	def __init__(self):
		hotel, restaurant, museum, attraction = Read_data()
		self.restaurant = restaurant
		self.hotel = hotel
		self.museum = museum
		self.attraction = attraction



	def Hotel_page_creator(self, lat, lng, price, value):
		#path = os.getcwd() + '/Data/bookingNYC.csv'
		#data_hotel = pd.read_csv(path, thousands = ',', encoding = 'latin1')
		if (value == 1):
			value_list = [1,2]
		elif (value == 2):
			value_list = [3,4]
		elif (value == 3):
			value_list = [5]
		df = sort_within(self.hotel, lat, lng, 3, price, value_list)
		draw_rader_chart_hotel(lat, lng, df)

	def Restaurant_page_creator(self, lat, lng, category, value):
		#path = os.getcwd() + '/Data/yelp_data.csv'
		#data_restaurant = pd.read_csv(path, encoding = 'latin1')
		yelp_category(self.restaurant)
		df = sort_within(self.restaurant, lat, lng, 2, category, value)
		draw_rader_chart_restaurant(lat, lng, df)

	def heatmap_creator(self, given_filter):
		draw_heatmap(given_filter)	

	def Museum_rtf_creator(self): 
		#path = os.getcwd() + '/Data/museum.csv'
		#museum = pd.read_csv(path, encoding = 'latin1')
		museum_sorted = sort_museums_or_attractions(self.museum)
		print_to_rtf(museum_sorted, 'Recommendation_museum')


	def Attraction_rtf_creator(self):
		#path = os.getcwd() + '/Data/attraction.csv'
		#attraction = pd.read_csv(path, encoding = 'latin1')
		attraction_sorted = sort_museums_or_attractions(self.attraction)
		print_to_rtf(attraction_sorted, 'Recommendation_attraction')

	def plot_recommendations_for_restaurants_in_map(self, lat, lng, category, value):
		#path = os.getcwd() + '/Data/yelp_data.csv'
		#data_restaurant = pd.read_csv(path, encoding = 'latin1')
		yelp_category(self.restaurant)
		df = sort_within(self.restaurant, lat, lng, 3, category, value)
		plot_map(df)

	def plot_recommendations_for_hotels_in_map(self, lat, lng, price, value):
		#path = os.getcwd() + '/Data/bookingNYC.csv'
		#data_restaurant = pd.read_csv(path, encoding = 'latin1')
		if (value == 1):
			value_list = [1,2]
		elif (value == 2):
			value_list = [3,4]
		elif (value == 3):
			value_list = [5]
		df = sort_within(self.hotel, lat, lng, 3, price, value_list)
		plot_map(df)

	def plot_recommendations_for_museums_in_map(self):
		#path = os.getcwd() + '/Data/museum.csv'
		#museum = pd.read_csv(path, encoding = 'latin1')
		museum_sorted = sort_museums_or_attractions(self.museum)
		plot_map(museum_sorted)

	def plot_recommendations_for_attractions_in_map(self):
		#path = os.getcwd() + '/Data/attraction.csv'
		#attraction = pd.read_csv(path, encoding = 'latin1')
		attraction_sorted = sort_museums_or_attractions(self.attraction)
		plot_map(attraction_sorted)	
