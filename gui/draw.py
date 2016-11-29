from rader_chart import * 
from sort import *
import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def draw_rader_chart_hotel(lat, lng, df):
    variables_hotel = ("Avgscore", "Clean", "Comfort", "Facilities", "Free_Wifi", "Staff", "Value_for_money",
            "Location", "Price")
    ranges_hotel = [(5, 10), (5, 10), (5, 10), (5, 10), (5, 10), 
            (5, 10), (5, 10), (5, 10),
            (0.00001, 5)] 

    data = list(zip(df.Avgscore, df.Cleanliness, df.Comfort, df.Facilities, df['Free Wifi'], df.Staff, df['Value for money'], df.Location, df.Price))
    information = list(zip(df.Name))

    pp = PdfPages('Recommendation_hotels.pdf')

    for i in range(len(data)):
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_hotel, ranges_hotel)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Hotel Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(bbox_inches='tight')

    pp.close()


def draw_rader_chart_restaurant(lat, lng, df):
    variables_restaurant = ('number_of_price', 'Reviews', 'score_of_review', 'Distance')
    ranges_restaurant = [(0.00001, 5), (0.00001, 5), (0.00001, 5), (0.00001, 10)]

    data = list(zip(df['number_of_price'], df['Reviews'], df['score_of_review'], df['Distance']))
    information = list(zip(df['restaurant_name']))

    pp = PdfPages('Recommendation_restaurants.pdf')

    for i in range(len(data)):
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_restaurant, ranges_restaurant)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Restaurant Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(bbox_inches='tight')

    pp.close()

