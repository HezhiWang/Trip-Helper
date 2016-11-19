import gmplot
import geopy
import pandas as pd
import numpy as np

def get_coordinates(places):
    places["latitude"] = place["address"].apply(get_lat)
    places["longitude"] = place["address"].apply(get_long)
    return places


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
    for index, row in places.iterrows:
        if row["ranking"] >= 4:
            high_lat.append(row["latitude"])
            high_long.append(row["longitude"])
        elif row["ranking"] <= 2:
            low_lat.append(row["latitude"])
            low_long.append(row["longitude"])
        else:
            med_lat.append(row["latitude"])
            med_long.append(row["longitude"])
    high_coordinates = [tuple(high_lat), tuple(high_long)]
    med_coorditates = [tuple(med_lat), tuple(med_long)]
    low_coordinates = [tuple(low_lat), tuple(low_long)]
    
    return high_coordinates, med_coorditates, low_coordinates 

def draw_heatmap(places):
    
    high_gradient = [(0,0,0,0),(0,255,0,1),(85,255,0,1),(170,255,0,1),(255,255,0,1),(255,170,0,1),(255,85,0,1),(255,0,0,1)]
    med_gradient = [(0,0,0,0),  (255, 255, 0, 1), (170, 255, 0, 1), (85,255,0,1), (0,255,0,1)]
    low_gradient = [(0,0,0,0), (0,255,0,1), (0,255,85,1), (0,255,170,1), (0,255,255,1), (0,170,255,1), (0,85,255,1), (0,0,255,1)]
    
    places = get_coordinates(places)
    center_lat = places["latitude"].mean()
    center_long = place["longitude"].mean()
    the_map = gmplot.GoogleMapPlotter(center_lat, center_long, 16)
    high_coordinates, med_coorditates, low_coordinates = rank_coordinates(places)
    
    if len(high_coordinates[0]) > 0 :
        the_map.heatmap(high_coordinates[0], high_coordinates[1], threshold=10, radius=50, gradient=high_gradient)
    
    if len(med_coordinates[0]) > 0 :
        the_map.heatmap(med_coordinates[0], med_coordinates[1], threshold=10, radius=50, gradient=med_gradient)
    
    if len(low_coordinates[0]) > 0 :
        the_map.heatmap(low_coordinates[0], low_coordinates[1], threshold=10, radius=50, gradient=low_gradient)
    the_map.draw("./heatmap.html")