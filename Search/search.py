from Plot.plot_rader_chart import *
from Plot.plot_to_rtf import *
from Plot.plot_map import *
from Sort.sort import *
from Sort.yelp_sort import *
import os
import sys
from Data.Read_data import *


class Page_creator:
	"""
	This class uses in the 'Search' function, it has the methods to create the pdf file with rader chart, 
	the rtf file of museums recommendations, 
	the html file which can open automatically in google chrome.
	"""
	def __init__(self):
		#constructor read hotel, restaurant, museum, attraction data
		hotel, restaurant, museum, attraction = Read_data()
		self.restaurant = restaurant
		self.hotel = hotel
		self.museum = museum
		self.attraction = attraction

	def Hotel_page_creator(self, lat, lng, price, value):
		#This method create a pdf file with rader chart containing ten near recommendated hotels.
		if (value == 1):
			value_list = [1,2]
		elif (value == 2):
			value_list = [3,4]
		elif (value == 3):
			value_list = [5]
		df = sort_within(self.hotel, lat, lng, 1.5, price, value_list)
		draw_rader_chart_hotel(lat, lng, df)

	def Restaurant_page_creator(self, lat, lng, category, value):
		#This method create a pdf file with rader chart containing ten near recommendated Restaurants.
		yelp_category(self.restaurant)
		df = sort_within(self.restaurant, lat, lng, 1.5, category, value)
		draw_rader_chart_restaurant(lat, lng, df)

	def Museum_rtf_creator(self): 
		#This method create a rtf file with rader chart containing ten near recommendated museums.
		museum_sorted = sort_museums_or_attractions(self.museum)
		print_to_rtf(museum_sorted, 'Recommendation_museum')


	def Attraction_rtf_creator(self):
		#This method create a rtf file with rader chart containing ten near recommendated attractions.
		attraction_sorted = sort_museums_or_attractions(self.attraction)
		print_to_rtf(attraction_sorted, 'Recommendation_attraction')

	def plot_recommendations_for_restaurants_in_map(self, lat, lng, category, value):
		"""
		This method create a html file, and it will automatically open in google chorme. 
		And ten recommendated restaurants will be marked in the google map.
		"""
		yelp_category(self.restaurant)
		df = sort_within(self.restaurant, lat, lng, 1.5, category, value)
		plot_map(df)

	def plot_recommendations_for_hotels_in_map(self, lat, lng, price, value):
		"""
		This method create a html file, and it will automatically open in google chorme. 
		And ten recommendated hotels will be marked in the google map.
		"""
		if (value == 1):
			value_list = [1,2]
		elif (value == 2):
			value_list = [3,4]
		elif (value == 3):
			value_list = [5]
		df = sort_within(self.hotel, lat, lng, 1.5, price, value_list)
		plot_map(df)

	def plot_recommendations_for_museums_in_map(self):
		"""
		This method create a html file, and it will automatically open in google chorme. 
		And ten recommendated museums will be marked in the google map.
		"""
		museum_sorted = sort_museums_or_attractions(self.museum)
		plot_map(museum_sorted)

	def plot_recommendations_for_attractions_in_map(self):
		"""
		This method create a html file, and it will automatically open in google chorme. 
		And ten recommendated attractions will be marked in the google map.
		"""
		attraction_sorted = sort_museums_or_attractions(self.attraction)
		plot_map(attraction_sorted)	
