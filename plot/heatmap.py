import gmplot
import geopy
import pandas as pd
import numpy as np
import os
import webbrowser
from geopy.geocoders.base import GeocoderServiceError


def get_lat(address):
    geolocator = geopy.geocoders.Nominatim()
    location = geolocator.geocode(address)
    return location.latitude
def get_long(address):
    geolocator = geopy.geocoders.Nominatim()
    location = geolocator.geocode(address)
    return location.longitude

def rank_coordinates(places):
    high_lat = []
    high_long = []
    med_lat = []
    med_long = []
    low_lat = []
    low_long = []
    for index, row in places.iterrows():
        if str(row["Lat"]) == "nan":
            pass
        else:
            if row["Avgscore"] >= 7:
                high_lat.append(row["Lat"])
                high_long.append(row["Lng"])
            elif row["Avgscore"] <= 4:
                low_lat.append(row["Lat"])
                low_long.append(row["Lng"])
            else:
                med_lat.append(row["Lat"])
                med_long.append(row["Lng"])
    high_coordinates = [tuple(high_lat), tuple(high_long)]
    med_coorditates = [tuple(med_lat), tuple(med_long)]
    low_coordinates = [tuple(low_lat), tuple(low_long)]
    
    return high_coordinates, med_coorditates, low_coordinates 

def draw_heatmap(csv_name):


    path = os.getcwd() + '/Data/' + csv_name + '.csv'
    data_restaurant = pd.read_csv(path, encoding = 'latin1')

    places = pd.read_csv(path, encoding = 'latin1', header = 0, index_col = 0)
    high_gradient = [(255, 255, 255,0),(255, 255, 0, 1),(255, 170, 0, 1),(255, 85, 0, 1), (255, 0, 0,1)]
    med_gradient = [(255, 255, 255,0),  (255, 255, 0, 1), (170, 255, 0, 1), (85,255,0,1), (0,255,0,1)]
    low_gradient = [(255, 255, 255,0),  (0,255,255,1), (0,170,255,1), (0,85,255,1), (0,0,255,1)]
    center_lat = places["Lat"].mean()
    center_long = places["Lng"].mean()
    the_map = gmplot.GoogleMapPlotter(center_lat, center_long, 11)
    high_coordinates, med_coordinates, low_coordinates = rank_coordinates(places)
    
    
    if len(high_coordinates[0]) > 0 :
        the_map.heatmap(high_coordinates[0],high_coordinates[1],threshold=10,radius=25, gradient=high_gradient)
    
    if len(med_coordinates[0]) > 0 :
        the_map.heatmap(med_coordinates[0], med_coordinates[1], threshold=10, radius=25, gradient=med_gradient)
    
    if len(low_coordinates[0]) > 0 :
        the_map.heatmap(low_coordinates[0], low_coordinates[1], threshold=10, radius=25, gradient=low_gradient)
    the_map.draw("./" + csv_name + "_heatmap.html")
    new = 2
    url = "./" + csv_name + "_heatmap.html"
    webbrowser.open(url,new=new)
    

#draw_heatmap("hotels")