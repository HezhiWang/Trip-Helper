import tkinter as tk
from PIL import ImageTk, Image
import PIL.Image
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
from tkinter import messagebox
import pandas as pd
from Search.search import *
from Exception.exception import * 
from Plan.trip_plan import *
from Plot.overview_plot import *
from Overview.plot_heatmap import *

"""
Reference: https://pythonprogramming.net/organizing-gui/
I learned the stuff in the above tutorial and write the following code to build our GUI
"""

LARGE_FONT= ("Verdana", 12)
lat = 0
logi = 0
Time = ""
Bugdet = ""
Degree = ""

class GUI(tk.Tk):
    """
    This is the base of the following classes and bulids the structure of the GUI.
    """
    def __init__(self, *args, **kwargs):
        #Constructor to build the structure of the GUI and create a list of frames we created in the following.        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, width = 20000, height = 15000)

        container.pack(fill="both", expand = True)

        self.frames = {}

        for F in (StartPage, Restaurant, Hotel, Attractions, Museums, Search, Plan, Overview, 
                    Plan_secondPage, Plan_ThirdPage, Overview_hotel, Overview_restaurant, Overview_attractions, Overview_museums):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage, 0, 0)

    def show_frame(self, cont, *args):

        #This method will show the frame when we call it.

        frame = self.frames[cont]
        self.lat = lat
        self.logi = logi
        frame.tkraise()

        
class StartPage(tk.Frame):
    
    """
    This class bulid the Home page of the GUI
    """

    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        root = tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to NYC!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)
 
        button1 = tk.Button(self, text="Search", height = 2, width = 10, bg='blue',
                            command=lambda: controller.show_frame(Search, 0, 0))
        button1.pack(pady=10,padx=10)

        button2 = tk.Button(self, text="Plan", height = 2, width = 10, bg='red',
                            command=lambda: controller.show_frame(Plan, 0, 0))
        button2.pack(pady=10,padx=10) 

        button3 = tk.Button(self, text="Overview", height = 2, width = 10, bg='yellow',
                            command=lambda: controller.show_frame(Overview, 0, 0))
        button3.pack(pady=10,padx=10) 

class Search(tk.Frame): 
    """
    This class bulids the first page in the 'Search' function. User will first enter their current latitude and longitude, then choose 
    one of the fields from 'Restaurant', 'hotel', 'museum', 'attraction' to search, and output the near recommendated infomration for users
    by polting map, creating a pdf file with rader chart.
    """
    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        root = tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Welcome to NYC! ", font=("Verdana", 20))
        label.pack(pady=35,padx=100)

        label = tk.Label(self, text="Please Enter Your Location: ", font=("Verdana", 16))
        label.pack(pady=5,padx=10)
        
        ents = []

        label1 = tk.Label(self, text="Latitude", font=("Arial Black", 16), anchor='w')
        label1.pack()
        
        e1 = tk.Entry(self)
        e1.pack()
        ents.append(e1)

        label2 = tk.Label(self, text="Longitude", font=("Arial Black", 16), anchor='w')
        label2.pack()
        
        e2 = tk.Entry(self)
        
        ents.append(e2)

        e2.pack()

        
        """
        button2 = tk.Button(self, text = 'Enter', command = lambda: self.fetch(ents))
        button2.pack(pady=20, padx=20)
        """
    
        label = tk.Label(self, text="Your latitude should be in [40.700, 40.854] and longitude in [-74.018, -73.929]", font=("Verdana", 12))
        label.pack()
        label4 = tk.Label(self, text="Examples:", font=16, anchor='w', justify=LEFT)
        label4.pack()        
        label4 = tk.Label(self, text="Empire State Buliding, Latitude: 40.748817, Longitude: -73.985428", font=LARGE_FONT, anchor='w', justify=LEFT)
        label4.pack()
        label5 = tk.Label(self, text="Central Park, Latitude: 40.785091, Longitude: -73.968285", font=LARGE_FONT, anchor='w', justify=LEFT)
        label5.pack()       
        label5 = tk.Label(self, text="Washington Square Park, Latitude: 40.730824, Longitude: -73.997330", font=LARGE_FONT, anchor='w', justify=LEFT)
        label5.pack() 

        label3 = tk.Label(self, text="Please select a type, then click 'search':", font=("Verdana", 16), anchor='w')
        label3.pack(pady=30,padx=20)
        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Restaurant')
        w.insert(2, 'Hotel')
        w.insert(3, 'Attraction')
        w.insert(4, 'Museum')

        button1 = tk.Button(self, text = "Search", width = 15,
                            command = lambda: self.button_command(w, controller, ents))

        button1.pack(side = LEFT, pady=20,padx=120)


        button1 = tk.Button(self, text="Back to Homepage", width = 15,
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(side = LEFT, pady=20,padx = 120) 

    def button_command(self, w, controller, entries):
        """
        This function pass the stuff chosen by users from the listbox and go to its corresponding page.

        Parameters: 
            w: tk.Listbox()
            controller
        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            global lat 
            lat = float(entries[0].get())
            global logi 
            logi = float(entries[1].get())
            if (-73.929 < logi or logi < -74.018):
                raise Invalidinput
            if (40.854 < lat or lat < 40.700):
                raise Invalidinput            

            if (not w.curselection()):
                raise IndexError                                  
            if w.get(w.curselection()) == 'Restaurant':
                controller.show_frame(Restaurant, lat, logi)                                       
            elif w.get(w.curselection()) == 'Hotel':
                controller.show_frame(Hotel, lat, logi)
            elif w.get(w.curselection()) == 'Attraction':
                controller.show_frame(Attractions, lat, logi)
            elif w.get(w.curselection()) == 'Museum':
                controller.show_frame(Museums, lat, logi) 
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")    
        except ValueError:
            messagebox.showwarning("Error", "Invalid input, please enter your correct longitude and latitude")  
        except Invalidinput:
            messagebox.showwarning("Error", "Invalid input, your longitude and latitude is out of range")


class Plan(tk.Frame):     
    """
    This class bulids the first page in the 'Plan' function. User will then choose several perefenrences, then we will design the travel route 
    for them automatically including the attractions, hotels and restaurant recommendations in a txt file.
    """
    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Customize Your Travel Plan", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose your travel time:", font=("Verdana", 16), anchor='w')
        label1.pack(pady=20,padx=40)
        w1 = tk.Listbox(self)
        w1.pack(pady=20)
        w1.insert(1, '1 Day')
        w1.insert(2, '2 Days')
        w1.insert(3, '3 Days')
        w1.insert(4, '4 Days')
        w1.insert(5, '5 Days')
        w1.insert(6, '6 Days')
        w1.insert(7, '7 Days')

        button1 = tk.Button(self, text="Next Page >>",
                            command=lambda: self.check_click(controller, w1))
        button1.pack(side = LEFT, pady=10,padx=120) 

        button2 = tk.Button(self, width = 15, text="Back to Homepage",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button2.pack(side = LEFT, pady=10,padx=120)  

    def combined_function(self, t, controller, w):
        """
        This function records the user choosed time period into global variable Time and go to the next page.
        """
        global Time
        Time = t
        controller.show_frame(Plan_secondPage, 0, 0)


    def check_click(self, controller, w1):
        """
        This function pass the user choosed time as parameters to method combined_function and call the combined_function method.

        Parameters: 
            w: tk.Listbox()
            controller
        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w1.curselection()):
                raise IndexError  
            if w1.get(w1.curselection()) == '1 Day': 
                self.combined_function(1, controller, w1)
            elif w1.get(w1.curselection()) == '2 Days':
                self.combined_function(2, controller, w1)
            elif w1.get(w1.curselection()) == '3 Days':
                self.combined_function(3, controller, w1)
            elif w1.get(w1.curselection()) == '4 Days':
                self.combined_function(4, controller, w1)
            elif w1.get(w1.curselection()) == '5 Days':
                self.combined_function(5, controller, w1)
            elif w1.get(w1.curselection()) == '6 Days':
                self.combined_function(6, controller, w1)
            elif w1.get(w1.curselection()) == '7 Days':
                self.combined_function(7, controller, w1)
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")  


class Plan_secondPage(tk.Frame):
    """
    This class bulids the second page in the 'Plan' function. User will then choose one perefenrence in this page, then go to the next page.
    """
    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI
        
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Please choose your budget", font=("Verdana", 20), anchor='w')
        label1.pack(pady=100,padx=100)
        w = tk.Listbox(self, font = 15)
        w.pack()
        w.insert(1, 'Tight')
        w.insert(2, 'Moderate')
        w.insert(3, 'Adequate')

        button1 = tk.Button(self, text="Next Page >>",
                            command=lambda: self.check_click1(controller, w))
        button1.pack(side = LEFT, padx=50) 

        button2 = tk.Button(self, text="Back to Previous Page <<",
                            command=lambda: controller.show_frame(Plan, 0, 0))
        button2.pack(side = LEFT, padx=50)  

        button3 = tk.Button(self, text="Back to Homepage",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button3.pack(side = LEFT, padx=50)

    def combined_function1(self, b, controller):
        """
        This function records the user choosed Budget into global variable Budget and go to the next page.
        """
        global Bugdet
        Bugdet = b
        controller.show_frame(Plan_ThirdPage, 0, 0)

    def check_click1(self, controller, w):
        """
        This function pass the user choosed time as parameters to method combined_function1 and call the combined_function1 method.

        Parameters: 
            w: tk.Listbox()
            controller
        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError  
            
            if w.get(w.curselection()) == 'Tight':           
                self.combined_function1(1, controller)
            elif w.get(w.curselection()) == 'Moderate':
                self.combined_function1(2, controller)
            elif w.get(w.curselection()) == 'Adequate':
                self.combined_function1(3, controller) 
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox") 

class Plan_ThirdPage(tk.Frame):
    """
    This class bulids the last page in the 'Plan' function. User will then choose one perefenrence in this page, then 
    we will design the travel route for them automatically including the attractions, hotels and 
    restaurant recommendations in a txt file.
    """

    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Please choose your preferred time arrangement:", font=("Verdana", 20), anchor='w')
        label1.pack(pady=100,padx=100)
        w = tk.Listbox(self, font = 15)
        w.pack()
        w.insert(1, 'Tight Schedule')
        w.insert(2, 'Flexible Schedule')

        button1 = tk.Button(self, text="Get your travel plan !",
                            command=lambda: self.check_click2(w))
        button1.pack(side = LEFT, pady=10,padx=50) 

        button2 = tk.Button(self, text="Back to previous page <<",
                            command=lambda: controller.show_frame(Plan_secondPage, 0, 0))
        button2.pack(side = LEFT, pady=20,padx=50)  

        button3 = tk.Button(self, text="Back to Homepage",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button3.pack(side = LEFT, pady=20,padx=50) 

    def check_click2(self, w):
        """
        This function choose the last paramter, and then call the trip_planer function to design the travel route 
        for users automatically including the attractions, hotels and restaurant recommendations based on their prefenrances, 
        and output the results in a txt file.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError  
            elif w.get(w.curselection()) == 'Tight Schedule':     
                t = trip_plan(Time, Bugdet, 2)
                t.trip_planer(Time, Bugdet, 2)
            elif w.get(w.curselection()) == 'Flexible Schedule':                         
                t = trip_plan(Time, Bugdet, 1)  
                t.trip_planer(Time, Bugdet, 1)
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")        

class Overview(tk.Frame):   
    """ 
    This class builds the frame 'Overview' to let users overview the informaiton from 'Restaurant', 'hotel', 'museum', 'attraction', and plot 
    our analysis into heatmap, histogram, and boxplot
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Overview", font=("Verdana", 20))
        label.pack(pady=100,padx=100)   
        
        w = tk.Listbox(self)

        w.insert(1, 'Hotel')
        w.insert(2, 'Restaurant')
        w.insert(3, 'Attraction')
        w.insert(4, 'Museum')
        w.pack(pady=50,padx=100, anchor = CENTER)


        button1 = tk.Button(self, text = "Show Plots!", width = 20,
                            command = lambda: self.check_click4(w, controller))
        button1.pack(side = LEFT, pady = 10, padx = 120) 
        

        button3 = tk.Button(self, text = "Back to Homepage",width = 15,
                            command = lambda: controller.show_frame(StartPage, 0, 0))
        button3.pack(side = LEFT, pady = 10, padx = 120) 

    def check_click4(self, w, controller):
        """
        This function let user choose what they want to overview from 'Restaurant', 'hotel', 'museum', 'attraction',
        and plot their heatmap in a html file, and open it automaticlly.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError

            if w.get(w.curselection()) == 'Restaurant':
                controller.show_frame(Overview_restaurant, lat, logi)                                       
            elif w.get(w.curselection()) == 'Hotel':
                controller.show_frame(Overview_hotel, lat, logi)
            elif w.get(w.curselection()) == 'Attraction':
                controller.show_frame(Overview_attractions, lat, logi)
            elif w.get(w.curselection()) == 'Museum':
                controller.show_frame(Overview_museums, lat, logi)   
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")  

class Overview_hotel(tk.Frame):
    """
    This class could plot five kinds of figures: heatmap, density figure, pie figure, number_of_rating_bar_figure, 
    rating_bar_figure.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="NYC Hotel Overview", font=("Verdana", 20))
        label.pack(pady=100,padx=100) 

        button1 = tk.Button(self, text="Show heatmap", height = 2, width = 25, bg='blue',
                            command=lambda: draw_heatmap('hotels'))
        button1.pack(pady=10,padx=10)

        o = overview_plot()

        button2 = tk.Button(self, text="Show density figure of reviews", height = 2, width = 40, bg='red',
                            command=lambda: o.plot_review_density('hotel'))
        button2.pack(pady=10,padx=10) 

        button3 = tk.Button(self, text="Show pie figure by price level", height = 2, width = 40, bg='yellow',
                            command=lambda: o.plot_pie('hotel'))
        button3.pack(pady=10,padx=10) 

        button4 = tk.Button(self, text="Show bar figure of ratings", height = 2, width = 40, bg='blue',
                            command=lambda: o.plot_rating_bar('hotel'))
        button4.pack(pady=10,padx=10)

        button5 = tk.Button(self, text="Show bar figure of average rating by price level", height = 2, width = 40, bg='red',
                            command=lambda: o.plot_bar_chart('hotel'))
        button5.pack(pady=10,padx=10)

        button6 = tk.Button(self, text="Back to Previous Page <<", height = 2, width = 40, bg='red',
                            command=lambda: controller.show_frame(Overview, 0, 0))
        button6.pack(pady=10,padx=10)

class Overview_restaurant(tk.Frame):
    """
    This class could plot five kinds of figures: heatmap, density figure, pie figure, number_of_rating_bar_figure, 
    rating_bar_figure.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="NYC Restaurant Overview", font=("Verdana", 20))
        label.pack(pady=100,padx=100)        

        button1 = tk.Button(self, text="Show heatmap", height = 2, width = 25, bg='blue',
                            command=lambda: draw_heatmap('restaurants'))
        button1.pack(pady=10,padx=10)

        o = overview_plot()

        button2 = tk.Button(self, text="Show density figure of reviews", height = 2, width = 40, bg='red',
                            command=lambda: o.plot_review_density('restaurant'))
        button2.pack(pady=10,padx=10) 

        button3 = tk.Button(self, text="Show pie figure by category", height = 2, width = 40, bg='yellow',
                            command=lambda: o.plot_pie('restaurant'))
        button3.pack(pady=10,padx=10) 

        button4 = tk.Button(self, text="Show bar figure of ratings", height = 2, width = 40, bg='blue',
                            command=lambda: o.plot_rating_bar('restaurant'))
        button4.pack(pady=10,padx=10)

        button5 = tk.Button(self, text="Show bar figure of average rating by price level", height = 2, width = 40, bg='red',
                            command=lambda: o.plot_bar_chart('restaurant'))
        button5.pack(pady=10,padx=10)

        button6 = tk.Button(self, text="Back to Previous Page <<", height = 2, width = 40, bg='red',
                            command=lambda: controller.show_frame(Overview, 0, 0))
        button6.pack(pady=10,padx=10)


class Overview_attractions(tk.Frame):
    """
    This class could plot five kinds of figures: heatmap, density figure, number_of_rating_bar_figure.
    """    
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="NYC Attraction Overview", font=("Verdana", 20))
        label.pack(pady=100,padx=100)    

        button1 = tk.Button(self, text="Show heatmap", height = 2, width = 25, bg='blue',
                            command=lambda: draw_heatmap('attractions'))
        button1.pack(pady=10,padx=10)

        o = overview_plot()

        button2 = tk.Button(self, text="Show density figure of reviews", height = 2, width = 25, bg='red',
                            command=lambda: o.plot_review_density('attraction'))
        button2.pack(pady=10,padx=10) 

        button4 = tk.Button(self, text="Show bar figure of ratings", height = 2, width = 25, bg='blue',
                            command=lambda: o.plot_rating_bar('attraction'))
        button4.pack(pady=10,padx=10)

        button4 = tk.Button(self, text="Back to Previous Page <<", height = 2, width = 25, bg='red',
                            command=lambda: controller.show_frame(Overview, 0, 0))
        button4.pack(pady=10,padx=10)           

class Overview_museums(tk.Frame):
    """
    This class could plot five kinds of figures: heatmap, density figure, number_of_rating_bar_figure.
    """    
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="NYC Museum Overview", font=("Verdana", 20))
        label.pack(pady=100,padx=100)  

        button1 = tk.Button(self, text="Show heatmap", height = 2, width = 25, bg='blue',
                            command=lambda: draw_heatmap('museums'))
        button1.pack(pady=10,padx=10)

        o = overview_plot()

        button2 = tk.Button(self, text="Show density figure of reviews", height = 2, width = 25, bg='red',
                            command=lambda: o.plot_review_density('museum'))
        button2.pack(pady=10,padx=10) 

        button4 = tk.Button(self, text="Show bar figure of ratings", height = 2, width = 25, bg='blue',
                            command=lambda: o.plot_rating_bar('museum'))
        button4.pack(pady=10,padx=10)

        button4 = tk.Button(self, text="Back to Previous Page <<", height = 2, width = 25, bg='red',
                            command=lambda: controller.show_frame(Overview, 0, 0))
        button4.pack(pady=10,padx=10)        

class Restaurant(tk.Frame):
    """ 
    This class builds the frame to 'Restaurant' let users choose the food category they want to know, 
    and then we will analyze our dataset and choose ten nearest and best restaurants for users via showing 
    a pdf file with reder chart and plot their locations in the map.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Find Nearby Restaurants", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose a category, then click 'search'", font=("Verdana", 16), anchor='w')
        label1.pack(pady=40,padx=40)

        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Chinese')
        w.insert(2, 'Japanese')
        w.insert(3, 'Asian')
        w.insert(4, 'Italian')
        w.insert(5, 'French')
        w.insert(6, 'American')    
        w.insert(7, 'European')
        w.insert(8, 'LatinAmerican')
        w.insert(9, 'Cafe & Bar')
        w.insert(10, 'African')
        w.insert(11, 'MiddleEastern')
        w.insert(12, 'Other')  

        p = Page_creator()

        button1 = tk.Button(self, text="Show the Map", width = 10,
                            command=lambda: self.check_botton1(w))

        button1.pack(side = LEFT, pady=20,padx=60)

        button2 = tk.Button(self, text="Show Recommendations", width = 20, anchor=CENTER,
                            command = lambda: self.check_botton2(w))

        button2.pack(side = LEFT, pady=20,padx=60)

        button3 = tk.Button(self, text="Back to Search <<", width = 20,
                            command=lambda: controller.show_frame(Search, 0, 0))

        button3.pack(side = LEFT, pady=20,padx=60)

    def check_botton1(self, w):
        """
        This function let users choose the food category they want to know, and after our analysis, to 
        recommend ten best restaurants in their neighborhood. By calling the plot_recommendations_for_restaurants_in_map
        function, we will automatically open our created html file in the google chorme.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError

            p = Page_creator()

            if w.get(w.curselection()) == 'Chinese':
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Chinese')
            elif w.get(w.curselection()) == 'Japanese':
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Japanese')
            elif w.get(w.curselection()) == 'Asian':
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Asian')
            elif w.get(w.curselection()) == 'Italian':    
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Italian')
            elif w.get(w.curselection()) == 'French':
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'French')  
            elif w.get(w.curselection()) == 'American':                 
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'US')
            elif w.get(w.curselection()) == 'European':                
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'European')
            elif w.get(w.curselection()) == 'LatinAmerican':
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'LatinAmerican')
            elif w.get(w.curselection()) == 'Cafe & Bar':                
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Cafe_bar')
            elif w.get(w.curselection()) == 'African':                
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'African')
            elif w.get(w.curselection()) == 'MiddleEastern':                
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'MiddleEastern')
            elif w.get(w.curselection()) == 'Other':                
                df = p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Other') 

            if df.empty:
                raise DataframeEmptyError

        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")  
        except DataframeEmptyError:
            messagebox.showwarning("Error", "")

    def check_botton2(self, w):
        """
        This function let users choose the food category they want to know, and after our analysis, to 
        recommend ten best restaurants in their neighborhood, and create the rader chart for each restaurant and 
        produce a pdf file by calling the Restaurant_page_creator.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError

            p = Page_creator()           
            if w.get(w.curselection()) == 'Chinese':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Chinese')
            elif w.get(w.curselection()) == 'Japanese':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Japanese')
            elif w.get(w.curselection()) == 'Asian':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Asian')
            elif w.get(w.curselection()) == 'Italian':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Italian')
            elif w.get(w.curselection()) == 'French':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'French')  
            elif w.get(w.curselection()) == 'American':                 
                p.Restaurant_page_creator(lat, logi, 'ctg', 'US')
            elif w.get(w.curselection()) == 'European':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'European')
            elif w.get(w.curselection()) == 'LatinAmerican':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'LatinAmerican')
            elif w.get(w.curselection()) == 'Cafe & Bar':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Cafe_bar')
            elif w.get(w.curselection()) == 'African':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'African')
            elif w.get(w.curselection()) == 'MiddleEastern':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'MiddleEastern')
            elif w.get(w.curselection()) == 'Other':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Other') 

        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")

class Hotel(tk.Frame):
    """ 
    This class builds the frame to 'Hotel' let users choose the budget of hotels they want to spend, 
    and then we will analyze our dataset and choose ten nearest and best hotels for users via showing 
    a pdf file with reder chart and plot their locations in the map.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Find Nearby Hotels", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose a price level, then click 'search'", font=("Verdana", 16), anchor='w')
        label1.pack(pady=40,padx=40)

        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Cheap')
        w.insert(2, 'Moderate')
        w.insert(3, 'Luxury')

        p = Page_creator()

        button1 = tk.Button(self, text="Show the Map", width = 10,
                            command=lambda: self.check_botton3(w))

        button1.pack(side = LEFT, pady=20,padx=60)

        button2 = tk.Button(self, text="Show Recommendations", width = 20,
                            command =
                            lambda: 
                                p.Hotel_page_creator(lat, logi, 'Price', 1)
                            if w.get(w.curselection()) == 'Cheap'          
                            else
                                p.Hotel_page_creator(lat, logi, 'Price', 2)
                            if w.get(w.curselection()) == 'Moderate'
                            else 
                                p.Hotel_page_creator(lat, logi, 'Price', 3)
                            if w.get(w.curselection()) == 'Luxury'
                            else 
                                print('haha'))
        
        button2.pack(side = LEFT, pady=20,padx=60)

        button3 = tk.Button(self, text="Back to Search <<", width = 20,
                            command=lambda: controller.show_frame(Search, 0, 0))
        button3.pack(side = LEFT, pady=20, padx=60)

    def check_botton3(self, w):
        """
        This function let users choose the hotel budget they want to know, and after our analysis, to 
        recommend ten best hotels in their neighborhood. By calling the plot_recommendations_for_hotels_in_map
        function, we will automatically open our created html file in the google chorme.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError

            p = Page_creator()

            if w.get(w.curselection()) == 'Cheap':
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 1)
            elif w.get(w.curselection()) == 'Moderate':                    
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 2)
            elif w.get(w.curselection()) == 'Luxury':                
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 3)
                              
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")
       
    def check_botton4(self, w):
        """
        This function let users choose the hotel budget they want to know, and after our analysis, to 
        recommend ten best hotels in their neighborhood. By calling the Hotel_page_creator
        function, we will create the rader chart for each restaurant and 
        produce a pdf file by calling the Restaurant_page_creator.

        Parameters: 
            w: tk.Listbox()

        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError

            p = Page_creator()

            if w.get(w.curselection()) == 'Cheap':
                p.Hotel_page_creator(lat, logi, 'Price', 1)
            if w.get(w.curselection()) == 'Moderate':
                p.Hotel_page_creator(lat, logi, 'Price', 2)
            if w.get(w.curselection()) == 'Luxury':                 
                p.Hotel_page_creator(lat, logi, 'Price', 3)
                      
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the items in the listbox")

class Attractions(tk.Frame):
    """
    This class creates the frame 'Attraction' under the 'search' function. User can click the button 'show the recommendations'
    to see the recommendation information of attractions written in a rtf file. User also can click the button 'show the map' to 
    see the recommnedated attractions' name and address in a html file. 
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Find NYC Attractions", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        p = Page_creator()

        button1 = tk.Button(self, text="Show Recommendations",
                            command=lambda: p.Attraction_rtf_creator())
        button1.pack(pady=30,padx=20) 

        button2 = tk.Button(self, text="Show the Map",
                            command=lambda: p.plot_recommendations_for_attractions_in_map())
        button2.pack(pady=30,padx=20)

        button3 = tk.Button(self, text="Back to Search <<",
                            command=lambda: controller.show_frame(Search, 0, 0))
        button3.pack(pady=30,padx=20)

class Museums(tk.Frame):
    """
    This class creates the frame 'Museum' under the 'search' function. User can click the button 'show the recommendations'
    to see the recommendation information of museums written in a rtf file. User also can click the button 'show the map' to 
    see the recommnedated museums' name and address in a html file. 
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Find NYC Museums", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        p = Page_creator()

        button1 = tk.Button(self, text="Show Recommendations",
                            command=lambda: p.Museum_rtf_creator())
        button1.pack(pady=30,padx=20) 

        button2 = tk.Button(self, text="Show the Map",
                            command=lambda: p.plot_recommendations_for_museums_in_map())
        button2.pack(pady=30,padx=20)

        button3 = tk.Button(self, text="Back to Search <<",
                            command=lambda: controller.show_frame(Search, 0, 0))
        button3.pack(pady=30,padx=20)


def main():
    try:
        app = GUI()
        app.mainloop()
    except KeyboardInterrupt:
        print('Control-C exiting')
        sys.exit()
    except EOFError:
        print('exiting')
        sys.exit()
if __name__ == "__main__": main()