from rader_chart import * 
from sort import *
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def draw_rader_chart(lat, lng, df, restaurant_or_hotel):
    variables_hotel = ("Avgscore", "Cleanliness_score", "Comfort_score", "Facilities_score", "Free_Wifi_score", "Staff_score", "Value_for_money_score",
            "Location_score", "Price")
    #d = distance_between_twopoints(lat, lng, 40.758854, -73.83081)
    #data = (8.4, 8.2, 7.9, 7.5, 9.2, 8.1, 7.5, 3, 7076)
    ranges_hotel = [(5, 10), (5, 10), (5, 10), (5, 10), (5, 10), 
            (5, 10), (5, 10), (5, 10),
            (1, 6)] 
    variables_restaurant = ('Distance', 'number_of_price', 'number_of_review', 'score_of_review')
    ranges_restaurant = [(0.1, 10), (1, 4), (0.1, 10000), (1, 5)]

    fig1 = plt.figure(figsize=(8, 8))
    if (restaurant_or_hotel == 1):
        data = list(zip(df.Avgscore, df.Cleanliness, df.Comfort, df.Facilities, df['Free Wifi'], df.Staff, df['Value for money'], df.Location, df.Price))
        radar = ComplexRadar(fig1, variables_hotel, ranges_hotel)
    elif (restaurant_or_hotel == 0):
        df['Distance'] = [distance_between_twopoints(lat, lng, df['latitude'].ix[i], df['longitude'].ix[i]) for i in range(df.shape[0])]
        data = list(zip(df.Distance, df['number_of_price'], df['number_of_review'], df['score_of_review']))
        radar = ComplexRadar(fig1, variables_restaurant, ranges_restaurant)
    radar.plot(data[0])
    radar.fill(data[0], alpha=0.3)
    plt.show()  
