from Plot.rader_chart import * 
from Sort.sort import *
import os
import numpy as np
import codecs
import matplotlib
import webbrowser
from selenium import webdriver
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def draw_rader_chart_hotel(lat, lng, df):
    """
    This function call the method in class 'ComplexRadar' to draw the rader chart for each recommend hotel,
    and create a pdf with hotels name and rader chart.

    Parameters:
        lat: float
        lng: float
        df: Dataframe

    Return:
        create a pdf file
    """
    variables_hotel = ("Avgscore", "Clean", "Comfort", "Facilities", "Free_Wifi", "Staff", "Value_for_money",
            "Location", "Price")
    ranges_hotel = [(5, 10), (5, 10), (5, 10), (5, 10), (5, 10), 
            (5, 10), (5, 10), (5, 10),
            (0.00001, 5)] 

    data = list(zip(df.Avgscore, df.Cleanliness, df.Comfort, df.Facilities, df['Free Wifi'], df.Staff, df['Value for money'], df.Location, df.Price))
    information = list(zip(df.Name))

    path = os.path.abspath("Results_recommendations")
    pp = PdfPages('Recommendation_hotels.pdf')

    for i in range(len(data)):
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_hotel, ranges_hotel)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Hotel Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(fname = path + '/Recommendation_hotels.pdf', bbox_inches = 'tight')
        plt.clf()
    pp.close()


def draw_rader_chart_restaurant(lat, lng, df):
    """
    This function call the method in class 'ComplexRadar' to draw the rader chart for each recommend restaurant,
    and create a pdf with restaurants name and rader chart.

    Parameters:
        lat: float
        lng: float
        df: Dataframe

    Return:
        create a pdf file
    """
    variables_restaurant = ('number_of_price', 'Reviews', 'score_of_review', 'Distance')
    ranges_restaurant = [(0.00001, 5), (0.00001, 5), (0.00001, 5), (0.00001, 10)]

    data = list(zip(df['number_of_price'], df['Reviews'], df['Avgscore'], df['Distance']))
    information = list(zip(df['Name']))

    path = os.path.abspath("Results_recommendations")
    pp = PdfPages('Recommendation_restaurants.pdf')

    for i in range(len(data)):
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_restaurant, ranges_restaurant)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Restaurant Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(fname = path + '/Recommendation_restaurants.pdf', bbox_inches = 'tight')
        plt.clf()
    pp.close()
