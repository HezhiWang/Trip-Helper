import unittest
from Sort.sort import *
from Sort.yelp_sort import *
from Data.Read_data import *
from Search.search import *

class tests(unittest.TestCase):

	"""Unit-testing class that allows us to run tests with expected outcomes
	Run the test in the project's root directory
	with the following command:
		$ python -m unittest discover
	"""
	def test_distance(self):
		"""
		This method tests the function distance in the Sort directory sort.py. 
		"""
		d1 = distance(40.748817, -73.985428, 40.785091, -73.968285)
		d2 = distance(40.785091, -73.968285, 40.730824, -73.997330)
		d3 = distance(40.748817, -73.985428, 40.730824, -73.997330)		

		self.assertEqual(2.659686800500446, d1)
		self.assertEqual(4.042818796866881, d2)
		self.assertEqual(1.3898520048298273, d3)

	def test_read_data_columnnames(self):
		"""
		This method tests the function Read_data in Data directory by tesing the read in dataframe has
		the same columns name as the original dataset.
		"""
		data_hotel, data_restaurant, data_museum, data_attraction = Read_data()

		hotel_columns = ['Unnamed: 0', 'Address', 'Avgscore', 'Cleanliness', 'Comfort', \
				'Facilities', 'Free Wifi', 'Location', 'Price', 'Staff', 'Total_review', \
				'Value for money', 'Lat', 'Lng', 'Name']
		restaurant_columns = ['Address', 'category', 'Lat', 'Lng', 'number_of_price', \
				'Total_review', 'Name', 'Avgscore']

		museum_columns = ['Unnamed: 0', 'Address', 'description', 'detail', 'Lat', 'Lng', 'Name', \
				'Avgscore', 'Total_review']

		attraction_columns = ['Unnamed: 0', 'Address', 'description', 'detail', 'Lat', 'Lng', 'Name', \
				'Avgscore', 'Total_review']
		
		self.assertEqual(hotel_columns, data_hotel.columns.tolist())
		self.assertEqual(restaurant_columns, data_restaurant.columns.tolist())
		self.assertEqual(museum_columns, data_museum.columns.tolist())
		self.assertEqual(attraction_columns, data_attraction.columns.tolist())
	
	def test_sort_within(self):
		"""
		This method tests the function sort_within in the sort.py in Sort directory by different perspectives.
		"""
		data_hotel, data_restaurant, data_museum, data_attraction = Read_data()

		df1 = sort_within(data_hotel, 40.748817, -73.985428, 1.5, 'Price', [1])

		"""
		This part tests the return dataframe contains the respected number of rows.
		"""
		yelp_category(data_restaurant)
		df2 = sort_within(data_restaurant, 40.748817, -73.985428, 1.5, 'ctg', 'Chinese')
		
		self.assertTrue(df1.shape[0] <= 10)
		self.assertTrue(df2.shape[0] <= 10)

		"""
		This part tests the sort_winthin method sort correctly. First, sort by 'Avgscore' column.
		If two values in the 'Avgscore' column are same, we compare their 'Total_review' values.
		"""

		for i in range(df1.shape[0]-1):
			self.assertTrue(df1.iloc[i]['Avgscore'] >= df1.iloc[i+1]['Avgscore'])
			if (df1.iloc[i]['Avgscore'] == df1.iloc[i+1]['Avgscore']):
				self.assertTrue(df1.iloc[i]['Total_review'] >= df1.iloc[i+1]['Total_review'])
			self.assertTrue(df2.iloc[i]['Avgscore'] >= df2.iloc[i+1]['Avgscore'])
			if (df2.iloc[i]['Avgscore'] == df2.iloc[i+1]['Avgscore']):
				self.assertTrue(df2.iloc[i]['Total_review'] >= df2.iloc[i+1]['Total_review'])

		cordinate_list1 = []
		cordinate_list2 = []
		"""
		This part tests the distance between each hotel or restaurant in the return dataframe and the center points
		is less than or equal to the parameter 'distance_within'. In this test, this parameter is 1.5
		"""
		for i in range(df1.shape[0]):
			self.assertTrue(distance(df1.iloc[i]['Lat'], df1.iloc[i]['Lng'], 40.748817, -73.985428) <= 1.5)
			self.assertTrue(distance(df2.iloc[i]['Lat'], df2.iloc[i]['Lng'], 40.748817, -73.985428) <= 1.5)

	def test_sort_museums_or_attractions(self):
		"""
		This method tests the sort function 'sort_museums_or_attraction' by variaties of perspectives.
		"""
		data_hotel, data_restaurant, data_museum, data_attraction = Read_data()

		df1 = sort_museums_or_attractions(data_museum)
		df2 = sort_museums_or_attractions(data_attraction)

		"""
		This part tests the return dataframe of the function 'sort_museums_or_attractions' has the following propetis:
		columns 'Avgscore' >= 3.5, column 'Total_review' >= 1000
		"""
		self.assertTrue((df1['Avgscore'] >= 3.5).all())
		self.assertTrue((df1['Total_review'] >= 1000).all())
		self.assertTrue((df2['Avgscore'] >= 3.5).all())
		self.assertTrue((df2['Total_review'] >= 1000).all())

		"""
		This part tests the function 'sort_museums_or_attractions' sort by rating and total reviews both descending.
		"""
		for i in range(df1.shape[0]-1):
			self.assertTrue(df1.iloc[i]['Avgscore'] >= df1.iloc[i+1]['Avgscore'])
			if (df1.iloc[i]['Avgscore'] == df1.iloc[i+1]['Avgscore']):
				self.assertTrue(df1.iloc[i]['Total_review'] >= df1.iloc[i+1]['Total_review'])
			self.assertTrue(df2.iloc[i]['Avgscore'] >= df2.iloc[i+1]['Avgscore'])
			if (df2.iloc[i]['Avgscore'] == df2.iloc[i+1]['Avgscore']):
				self.assertTrue(df2.iloc[i]['Total_review'] >= df2.iloc[i+1]['Total_review'])

	def test_yelp_category(self):
		"""
		This method tests the 'yelp_category' function in the Sort directory.
		"""
		data_hotel, data_restaurant, data_museum, data_attraction = Read_data()
		yelp_category(data_restaurant)

		restaurant_data_columns = ['Address', 'category', 'Lat', 'Lng', 'number_of_price', 
							'Total_review', 'Name', 'Avgscore', 'first_category', 'ctg']

		Category = ['Chinese','Japanese','Asian','Italian', 'French', 'US', \
					'European', 'LatinAmerican', 'Cafe_bar', 'African', 'MiddleEastern', 'Other']
		self.assertEqual(restaurant_data_columns, data_restaurant.columns.tolist())

		self.assertEqual(len(data_restaurant['ctg'].value_counts().index.tolist()), len(Category))

		


if __name__ == "__main__":
    unittest.main()

