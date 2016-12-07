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
                inner = True
                while inner:
                    try :
                        geolocator = geopy.geocoders.Nominatim()
                        location = geolocator.geocode(row["Name"] + ", New York")
                        places.loc[index, "Lat"] = location.latitude
                        places.loc[index, "Lng"] = location.longitude
                    except AttributeError: 
                        places.loc[index, "Lat"] = np.nan
                        places.loc[index, "Lng"] = np.nan
                        inner = False
                    except OSError:
                        pass
                    except GeocoderServiceError:
                        pass
                    else:
                        inner = False
                else :
                    timeouts = False
            except OSError:
                pass
            except GeocoderServiceError:
                pass
            else:
                timeouts = False
            
    return places

def get_score_column(df) :
    for name in ("Avgscore", "rating", "Rating"):
        if name in df.columns.values:
            score = name
    else:
        return df.rename(columns = {score : "Avgscore"})
        
def score_scaler(df):
    def time2(x):
        return 2 * x
    if df["Avgscore"].max() <= 5:
        df["Avgscore"] = df["Avgscore"].apply(time2)
    return df
def rewriter(input_file, output):
    old_df = pd.read_csv(input_file, header = 0, encoding = "latin1" )
    valid = False
    while not valid :
        ans = input("Do you want to get new coordinates?" + "\n")
        if ans[0] in ("y", "Y", "1"):
            old_df = get_coordinates(old_df)
            valid = True
        elif ans[0] in ("n", "N", "0"):
            valid = True
        else: 
            print("Invalid answer, type y or n")
            
    
    old_df = get_score_column(old_df)
    old_df = score_scaler(old_df)
    print("coordinates done")
    new_df = old_df[["Address", "Lat", "Lng", "Name", "Avgscore"]]
    new_df.to_csv(path_or_buf = output, na_rep = "nan")
    
def get_old_name():
    input_string = input("file to change?" + "\n")
    if input_string[-4:] == ".csv":
        return input_string
    else:
        raise ValueError("incorrect file name")

def get_new_name():
    input_string = input("new file name?" + "\n")
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