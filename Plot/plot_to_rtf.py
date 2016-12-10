from Plot.rader_chart import * 
from Sort.sort import *
from Data.Read_data import *
import os
import numpy as np
import codecs
import matplotlib
import webbrowser
from selenium import webdriver

def print_to_rtf(df, filename):

    """
    This function read the sorted information from parameter df, then write it to a rtf file
    with name 'filename'.
    
    Return:
        print sorted museums/attractions to rtf file
    
    Parameter:
        df: Dataframe
        filename =='museum' or 'attraction'
         
    Exception:
        IOError    
    """
    
    # replace - "-999" -> "NA"
    df = df.replace(to_replace= '-999', value='N.A.')
    # open file
    try:
        path = os.path.abspath("Results")
        rtf = open(path + '/' + filename+'.rtf', 'w')
        # header info
        rtf.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}}')
        for i in range(df.shape[0]):
            rtf.write(r'\ \b {} \b0 \line \ \b Rating:\b0 {} \t \b Reviews:\b0 {} \line'.format(df['Name'].iloc[i],
                   df['rating'].iloc[i], df['total_review'].iloc[i]))
            rtf.write(r'\ \b Details: \b0 {} \line\ \b Description: \b0 {} \line'.format(df['detail'].iloc[i],
                                                                        df['description'].iloc[i]))
            rtf.write(r'\line')
        rtf.write(r'}\n\x00')
    except IOError:
        print("Error: can\'t find file or read data")
    else:
        print("Written content in the file successfully")
        rtf.close()

def write_trip_plan_to_rtf(index_list, recommendation_order, recommended_center, recommended_attraction, bugdet_list): 
    """
    This function get the calculated recommended attractions from parameters. Based on each day's center points
    of attractions, we get the recommend hotels and restaurants for the corresponding day. Finally, we write the
    recommend attractions, hotels, restaurants to a rtf file.

    Parameters:
        index_list: list of list of int
        recommendation_order: list of int
        recommended_center: list of list of float
        recommended_attraction: dataframe

    Return:
        create a rtf file in 'Results' directory.
    """
    try:
        hotel, restaurant, museum, attraction = Read_data()
        path = os.path.abspath('Results')
        f = open(path + '/Trip_Plan.rtf','w')
        f.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}}')

        for i, item in enumerate(recommended_center):
            hotel_sorted = sort_within(hotel, item[0], item[1], 2, 'Price', bugdet_list)
            recommended_hotel = hotel_sorted.reindex(np.random.permutation(hotel_sorted.index))[:2]

            restaurant_sorted = sort_within(restaurant, item[0], item[1], 3)
            recommended_restaurant = restaurant_sorted.reindex(np.random.permutation(restaurant_sorted.index))[:3]

            f.write(r' \b {:*^100} \b0 \line\ '.format('DAY'+str(i+1)))
            f.write(r'\b Attractions: \b0 \line\ ')
            for x in index_list[recommendation_order[i]]:
                f.write(r'{} \line\ '.format(recommended_attraction.iloc[x]['name']))
                f.write(r'Address: \enspace {} \line\ '.format(recommended_attraction.iloc[x]['address']))
                f.write(r'Description: \enspace {} \line\ '.format(recommended_attraction.iloc[x]['description']))
                f.write(r'Detail: \enspace {} \line \line\ '.format(recommended_attraction.iloc[x]['detail']))

            f.write(r'\b Hotel: \b0 \line\ ')
            for x in range(2):
                f.write(r'{} \line\ '.format(recommended_hotel.iloc[x]['Name']))
                f.write(r'Address: \enspace {} \line\ '.format(recommended_hotel.iloc[x]['Address']))
                f.write(r'Score: \enspace {} \line\ '.format(recommended_hotel.iloc[x]['Avgscore']))
                f.write(r'Reviews: \enspace {} \line\ \line\ '.format(recommended_hotel.iloc[x]['Total_review']))

            f.write(r'\b Restaurant: \b0 \line\ ')
            for x in range(3):

                f.write(r'{} \line\ '.format(recommended_restaurant.iloc[x]['Name']))
                f.write(r'Address: \enspace {} \line\ '.format(recommended_restaurant.iloc[x]['Address']))
                f.write(r'Score: \enspace {} \line\ '.format(recommended_restaurant.iloc[x]['Avgscore']))
                f.write(r'Reviews: \enspace {} \line\ \line\ '.format(recommended_restaurant.iloc[x]['Total_review']))
            f.write(r'\line\ \line\ ')

        f.write(r'}\n\x00')
    except IOError:
        print("Error: can\'t find file or read data")
    else:
        print("Written content in the file successfully")       
        f.close()