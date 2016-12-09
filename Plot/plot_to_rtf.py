from Plot.rader_chart import * 
from Sort.sort import *
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
        path = os.path.abspath("Results_recommendations")
        rtf = open(path + filename+'.rtf', 'w')
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