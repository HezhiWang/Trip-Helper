import gmplot
import geopy
import pandas as pd
import numpy as np
from geopy.geocoders.base import GeocoderServiceError

def get_coordinates(places):
    
    for index, row in places.iterrows():
        
        timeouts = True 
        while timeouts:
            
            try:
                geolocator = geopy.geocoders.Nominatim()
                location = geolocator.geocode(row["Address"])
                places.loc[index, "Lat"] = location.latitude
                places.loc[index, "Lng"] = location.longitude
            except AttributeError:
                places.loc[index, "Lat"] = np.nan
                places.loc[index, "Lng"] = np.nan
                timeouts = False
            except OSError:
                pass
            except GeocoderServiceError:
                pass
            else:
                timeouts = False
            
    return places

def rewriter(input_file, output):
    old_df = pd.read_csv(input_file, header = 0, index_col = 0)
    old_df = get_coordinates(old_df)
    print("coordinates done")
    new_df = old_df[["Address", "Lat", "Lng", "Name", "Avgscore"]]
    new_df.to_csv(path_or_buf = output, na_rep = "nan")
    
def get_old_name():
    input_string = input("file to change?")
    if input_string[-4:] == ".csv":
        return input_string
    else:
        raise ValueError("incorrect file name")

def get_new_name():
    input_string = input("new file name?")
    if input_string[-4:] == ".csv":
        return input_string
    else:
        raise ValueError("incorrect file name")

valid = False

while not valid :
    try:
        input_file = get_old_name()
    except ValueError:
        print("incorrect file name entered")
    else:
        valid = True

valid = False

while not valid :
    try:
        output = get_new_name()
    except ValueError:
        print("incorrect file name entered")
    else:
        valid = True
        
rewriter(input_file, output)