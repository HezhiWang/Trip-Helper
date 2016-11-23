from draw import *
from sort import *
import os



def page_creator(lat, lng, given_filter, value):
	path1 = os.getcwd() + '/Data/bookingNYC.csv'
	data_hotel = pd.read_csv(path1, thousands = ',')

	if (value == 1):
		value_list = [1,2]
	elif (value == 2):
		value_list = [3,4]
	elif (value == 3):
		value_list = [5]
	df = sort_within(data_hotel, lat, lng, 3, given_filter, value_list)
	draw_rader_chart(lat, lng, df, 1)

