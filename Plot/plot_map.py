from Plot.rader_chart import * 
from Sort.sort import *
import os
import numpy as np
import codecs
import matplotlib
import webbrowser
from selenium import webdriver

def plot_map(df):
    '''
    This function creates a html file contain all in data in dataframe,
    then it will open automatically in google chrome, and recommendated information will
    be marked in google map.

    Parameter:   
        df is the dataframe(sorted nearby locations) with lat & lng
    Exception:
        IOError
    '''
    path = os.path.abspath("plot")
    try:
        fh = codecs.open(path + '/locations.js','w', "utf-8")
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
        base = os.getcwd()
        link = 'file://' + base + '/plot/plot_map.html' 
        webbrowser.open_new_tab(link)
    except IOError:
        print("Error: can\'t find file or read data")          
    except webbrowser.Error:
        print("Error: can't open web browser.")