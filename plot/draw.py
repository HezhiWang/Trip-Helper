from plot.rader_chart import * 
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
        plt.clf()
    pp.close()


def draw_rader_chart_restaurant(lat, lng, df):
    variables_restaurant = ('number_of_price', 'Reviews', 'score_of_review', 'Distance')
    ranges_restaurant = [(0.00001, 5), (0.00001, 5), (0.00001, 5), (0.00001, 10)]

    data = list(zip(df['number_of_price'], df['Reviews'], df['Avgscore'], df['Distance']))
    information = list(zip(df['Name']))

    pp = PdfPages('Recommendation_restaurants.pdf')

    for i in range(len(data)):
        fig = plt.figure(i, figsize=(4, 6))
        rader = ComplexRadar(fig, variables_restaurant, ranges_restaurant)
        rader.plot(data[i])
        rader.fill(data[i], alpha=0.2)
        text = 'Restaurant Name: ' + str(information[i][0])
        fig.text(0, 0.9, text, fontsize=15, fontweight='bold', color = 'blue')
        pp.savefig(bbox_inches='tight')
        plt.clf()
    pp.close()

def print_to_rtf(df, filename):
    '''print sorted museums/attractions to rtf file ,filename =='museum' or 'attraction' '''
    
    # replace - "-999" -> "NA"
    df = df.replace(to_replace= '-999', value='N.A.')
    # open file
    rtf = open(filename+'.rtf', 'w')
    # header info
    rtf.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}}')
    for i in range(df.shape[0]):
        rtf.write(r'\ \b {} \b0 \line \ \b Rating:\b0 {} \t \b Reviews:\b0 {} \line'.format(df['Name'].iloc[i],
               df['rating'].iloc[i], df['total_review'].iloc[i]))
        rtf.write(r'\ \b Details: \b0 {} \line\ \b Description: \b0 {} \line'.format(df['detail'].iloc[i],
                                                                    df['description'].iloc[i]))
        rtf.write(r'\line')
    rtf.write(r'}\n\x00')
    rtf.close()

def plot_map(df):
    '''df is the dataframe(sorted nearby locations) with lat & lng'''
    fh = codecs.open('locations.js','w', "utf-8")
    fh.write("locations = [\n")
    count = 0
    output= []

    for i in range(df.shape[0]):
        lat = df['Lat'].iloc[i]
        lng = df['Lng'].iloc[i]
        name = df['Name'].iloc[i]
        address = df['Address'].iloc[i].strip()
        
        output = "["+str(lat)+","+str(lng)+", \""+name+"\", "+ "\""+str(address)+"\"]"
        fh.write(output)
        if i < df.shape[0]-1:
            fh.write(",\n")
        else:
            fh.write("\n];\n")
            fh.close()
    #base = os.getcwd()
    #f=codecs.open('plot_map.html', 'r')
    #new = 2
    base = os.getcwd()
    link = 'file://' + base + '/plot/plot_map.html' 
    #webbrowser.open(link,new=new)
    webbrowser.open_new_tab(link)
    #chromedriver = os.path.abspath("Downloads/chromedriver")        
    """
    chromedriver = '/Users/wanghezhi/Downloads/chromedriver'
    #os.environ["webdriver.chrome.driver"] = chromedriver
    #os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    base = os.getcwd()
    link = 'file://'+base+ '/plot_map.html'
    driver.get(link)
    """