from rader_chart import * 
from sort import *
import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def draw_rader_chart(lat, lng, df, restaurant_or_hotel):
    variables_hotel = ("Avgscore", "Clean", "Comfort", "Facilities", "Free_Wifi", "Staff", "Value_for_money",
            "Location", "Price")
    #d = distance_between_twopoints(lat, lng, 40.758854, -73.83081)
    #data = (8.4, 8.2, 7.9, 7.5, 9.2, 8.1, 7.5, 3, 7076)
    ranges_hotel = [(5, 10), (5, 10), (5, 10), (5, 10), (5, 10), 
            (5, 10), (5, 10), (5, 10),
            (0.00001, 5)] 
    variables_restaurant = ('Distance', 'number_of_price', 'number_of_review', 'score_of_review')
    ranges_restaurant = [(0.1, 10), (1, 4), (0.1, 10000), (0.0001, 5)]
    
    #fig = []
    #for i in range(df.shape[0]):
    #    fig.append(plt.figure(i, figsize=(6, 6)))
    #rader = []
    if (restaurant_or_hotel == 1):
        data = list(zip(df.Avgscore, df.Cleanliness, df.Comfort, df.Facilities, df['Free Wifi'], df.Staff, df['Value for money'], df.Location, df.Price))
        information = list(zip(df.Name))
        #for i in range(df.shape[0]):
        #    rader.append(ComplexRadar(fig[i], variables_hotel, ranges_hotel))
    """
    elif (restaurant_or_hotel == 0):
        df['Distance'] = [distance_between_twopoints(lat, lng, df['latitude'].ix[i], df['longitude'].ix[i]) for i in range(df.shape[0])]
        data = list(zip(df.Distance, df['number_of_price'], df['number_of_review'], df['score_of_review']))
        information = list(zip(df['restaurant_name'], df.address))
        radar.append(ComplexRadar(fig1, variables_restaurant, ranges_restaurant))
    """
    pp = PdfPages('Recommendation_hotels.pdf')

    for i in range(len(data)):
        #plt.subplot(223)
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_hotel, ranges_hotel)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Hotel Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(bbox_inches='tight')
    """
    ,  bbox={'facecolor':'blue', 'alpha':0.5, 'pad':10}
    
    fig = plt.figure(figsize=(6, 6))
    
    rader = ComplexRadar(fig, variables_hotel, ranges_hotel)
    rader.plot(data[0])
    rader.fill(data[0], alpha=0.2)
    #ax = fig.add_subplot(223)
    #ax.legend(information[0], bbox_to_anchor=(0, 1), loc='upper right')
    #plt.legend(labels = information[0], loc = 7, prop = {'size': 15}, fancybox=True)
    fig.text(0.5, 0, str(information[0]), fontsize=30, fontweight='bold',  bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    #ax.text(8,8,information[0], style='italic',
    #    bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
    plt.show()
    pp.savefig()
    """
    pp.close()

