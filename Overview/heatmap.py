import gmplot
import pandas as pd
import numpy as np
import os
import webbrowser



def rank_coordinates(places):
    """This function groupes the coordinates based off of their rank"""
    high_lat = []
    high_long = []
    med_lat = []
    med_long = []
    low_lat = []
    low_long = []
    
    for index, row in places.iterrows():
        # Here the program ignores any nan coordinates
        if str(row["Lat"]) == "nan":
            pass
        else:
            
            # This where the places that are considered "good" have their coordinates registered
            if row["Avgscore"] >= 7:
                high_lat.append(row["Lat"])
                high_long.append(row["Lng"])
                
            # This where the places that are considered "bad" have their coordinates registered
            elif row["Avgscore"] <= 4 and row["Avgscore"] >= 0 :
                low_lat.append(row["Lat"])
                low_long.append(row["Lng"])
                
            # This where the places that are considered "alright" or have no rank
            # have their coordinates registered
            else:
                med_lat.append(row["Lat"])
                med_long.append(row["Lng"])
    # Placed the coordnates in this fashion for ease of reading later
    high_coordinates = [tuple(high_lat), tuple(high_long)]
    med_coorditates = [tuple(med_lat), tuple(med_long)]
    low_coordinates = [tuple(low_lat), tuple(low_long)]
    
    return high_coordinates, med_coorditates, low_coordinates 

def draw_heatmap(csv_name):
    """This function reads the csv with coordinates and rank of several places and then creates a heatmap        which is then displayed in the user's browser"""

    # Here the function gets the path for the csv
    path = os.getcwd() + '/Data/' + csv_name + '.csv'
    
    # Here the function reads the csv into a dataframe
    try:
        places = pd.read_csv(path, encoding = 'latin1', header = 0, index_col = 0)
    except OSError:
        print("file for option not found")
        
    # Here the function defines the color gradient for different layers of the heatmap
    high_gradient = [(255, 255, 255,0),(255, 255, 0, 1),(255, 170, 0, 1),(255, 85, 0, 1), (255, 0, 0,1)]
    med_gradient = [(255, 255, 255,0),  (255, 255, 0, 1), (170, 255, 0, 1), (85,255,0,1), (0,255,0,1)]
    low_gradient = [(255, 255, 255,0),  (0,255,255,1), (0,170,255,1), (0,85,255,1), (0,0,255,1)]
    
    # Here the center point for the map is defined
    center_lat = 40.7128
    center_long = -74.0059
    
    # Here the map is created and the coordinates are split into groups based off of their rank
    the_map = gmplot.GoogleMapPlotter(center_lat, center_long, 11)
    
    try:
        high_coordinates, med_coordinates, low_coordinates = rank_coordinates(places)
    except KeyError:
        print("Csv that was read did not have proper name for columns")
        
    
    # These nex couple of lines are to make sure that no the function does no try to write any empty 
    # groups on to the heatmap
    if len(high_coordinates[0]) > 0 :
        the_map.heatmap(high_coordinates[0],high_coordinates[1],threshold=10,radius=25, gradient=high_gradient)
    
    if len(med_coordinates[0]) > 0 :
        the_map.heatmap(med_coordinates[0], med_coordinates[1], threshold=10, radius=25, gradient=med_gradient)
    
    if len(low_coordinates[0]) > 0 :
        the_map.heatmap(low_coordinates[0], low_coordinates[1], threshold=10, radius=25, gradient=low_gradient)
    
    # The heatmap is drawn here
    path = os.path.abspath('Results')
    the_map.draw(path + '/' + csv_name + "_heatmap.html")

    # Here the heatmap is opened up in the user's browser
    link = 'file://'+ path + '/'+csv_name + "_heatmap.html" 
    webbrowser.open_new(link)

