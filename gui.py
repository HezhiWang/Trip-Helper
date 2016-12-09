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
from exception import * 
from Plan.trip_plan import *
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

        for F in (StartPage, Restaurant, Hotel, Attractions, Museums, Search, Plan, Overview, Plan_secondPage, Plan_ThirdPage):

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
    This class bulid in the first page of the GUI
    """

    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        root = tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to NYC", font=("Verdana", 20))
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

        #add a jpg figure to GUI reference: http://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
        
        #window = tk.Tk()
        #window.title("Join")
        #window.geometry("300x100")
        #window.configure(background='white')
        """
        try:
            path = os.getcwd()
            file = path + "/nyc skyline.jpg"

            img = ImageTk.PhotoImage(PIL.Image.open(file))

            p = tk.Label(self, image = img)
            #p.image = img
            p.pack(side = "bottom")
        except IOError:
            pass
        """


class Search(tk.Frame): 
    """
    This class bulids the first page in the 'Search' function. User will first enter their current latitude and longitude, then choose 
    one of the fields from 'Restaurant', 'hotel', 'museum', 'attraction' to search, and output the near recommendated infomration for users
    by polting map, creating a pdf file with rader chart.
    """
    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        root = tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to NYC", font=("Verdana", 20))
        label.pack(pady=80,padx=100)

        label = tk.Label(self, text="Please enter your location (you could look at those examples), then click 'Enter'", font=("Verdana", 16))
        label.pack(pady=20,padx=20)

        ents = []

        label1 = tk.Label(self, text="Latitude", font=LARGE_FONT, anchor='w')
        label1.pack()
        
        e1 = tk.Entry(self)
        e1.pack()
        ents.append(e1)

        label2 = tk.Label(self, text="Longitude", font=LARGE_FONT, anchor='w')
        label2.pack()
        
        e2 = tk.Entry(self)
        
        ents.append(e2)

        e2.pack()

        button2 = tk.Button(self, text = 'Enter', command = lambda: self.fetch(ents))
        button2.pack(pady=20, padx=20)

        label4 = tk.Label(self, text="Examples:", font=16, anchor='w', justify=LEFT)
        label4.pack()        
        label4 = tk.Label(self, text="Empire State Buliding, Latitude: 40.748817, Longitude: -73.985428", font=LARGE_FONT, anchor='w', justify=LEFT)
        label4.pack()
        label5 = tk.Label(self, text="Central Park, Latitude: 40.785091, Longitude: -73.968285", font=LARGE_FONT, anchor='w', justify=LEFT)
        label5.pack()       
        label5 = tk.Label(self, text="Washington Square Park, Latitude: 40.730824, Longitude: -73.997330", font=LARGE_FONT, anchor='w', justify=LEFT)
        label5.pack() 

        label3 = tk.Label(self, text="Please choose what you want to know, then click 'search'", font=("Verdana", 16), anchor='w')
        label3.pack(pady=20,padx=20)
        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Restaurant')
        w.insert(2, 'Hotel')
        w.insert(3, 'Attractions')
        w.insert(4, 'Museums')

        button1 = tk.Button(self, text = "Search",
                            command = lambda: self.button_command(w, controller))

        button1.pack(side = LEFT, pady=20,padx=70)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(side = RIGHT, pady=20,padx = 70) 

    def fetch(self, entries):
        """
        This function record the input longitude and latitude from users.

        Parameters: 
            entries: tk.Entry()

        Execptions:
            catch ValueError exceptions
        """
        try:
            global lat 
            lat = float(entries[0].get())
            global logi 
            logi = float(entries[1].get())
        except ValueError:
            messagebox.showwarning("Error", "Invalid input, please enter your correct langitude and latitude")  

    def button_command(self, w, controller):
        """
        This function pass the stuff chosen by users from the listbox and go to its corresponding page.

        Parameters: 
            w: tk.Listbox()
            controller
        Execptions:
            catch IndexError exceptions to let user choose some stuff in the listbox
        """
        try:
            if (not w.curselection()):
                raise IndexError                                  
            if w.get(w.curselection()) == 'Restaurant':
                controller.show_frame(Restaurant, lat, logi)                                       
            elif w.get(w.curselection()) == 'Hotel':
                controller.show_frame(Hotel, lat, logi)
            elif w.get(w.curselection()) == 'Attractions':
                controller.show_frame(Attractions, lat, logi)
            elif w.get(w.curselection()) == 'Museums':
                controller.show_frame(Museums, lat, logi) 
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")    

class Plan(tk.Frame):     
    """
    This class bulids the first page in the 'Plan' function. User will then choose several perefenrences, then we will design the travel route 
    for them automatically including the attractions, hotels and restaurant recommendations in a txt file.
    """
    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bulid you travel plan!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose the travel time:", font=("Verdana", 16), anchor='w')
        label1.pack(pady=20,padx=40)
        w1 = tk.Listbox(self)
        w1.pack(pady=20)
        w1.insert(1, '1 Day')
        w1.insert(2, '2 Day')
        w1.insert(3, '3 Day')
        w1.insert(4, '4 Day')
        w1.insert(5, '5 Day')
        w1.insert(6, '6 Day')
        w1.insert(7, '7 Day')

        button1 = tk.Button(self, text="Go to next Perference",
                            command=lambda: self.check_click(controller, w1))
        button1.pack(side = LEFT, pady=10,padx=120) 

        button2 = tk.Button(self, width = 15, text="Back to Home",
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
            elif w1.get(w1.curselection()) == '2 Day':
                self.combined_function(2, controller, w1)
            elif w1.get(w1.curselection()) == '3 Day':
                self.combined_function(3, controller, w1)
            elif w1.get(w1.curselection()) == '4 Day':
                self.combined_function(4, controller, w1)
            elif w1.get(w1.curselection()) == '5 Day':
                self.combined_function(5, controller, w1)
            elif w1.get(w1.curselection()) == '6 Day':
                self.combined_function(6, controller, w1)
            elif w1.get(w1.curselection()) == '7 Day':
                self.combined_function(7, controller, w1)
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")  


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
        w.insert(1, 'Economy')
        w.insert(2, 'Ordinary')
        w.insert(3, 'Luxury')

        button1 = tk.Button(self, text="Go to next Perference",
                            command=lambda: self.check_click1(controller, w))
        button1.pack(side = LEFT, padx=50) 

        button2 = tk.Button(self, text="Back to previous page",
                            command=lambda: controller.show_frame(Plan, 0, 0))
        button2.pack(side = LEFT, padx=50)  

        button3 = tk.Button(self, text="Back to home page",
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
            
            if w.get(w.curselection()) == 'Economy':           
                self.combined_function1(1, controller)
            elif w.get(w.curselection()) == 'Ordinary':
                self.combined_function1(2, controller)
            elif w.get(w.curselection()) == 'Luxury':
                self.combined_function1(3, controller) 
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox") 

class Plan_ThirdPage(tk.Frame):
    """
    This class bulids the last page in the 'Plan' function. User will then choose one perefenrence in this page, then 
    we will design the travel route for them automatically including the attractions, hotels and 
    restaurant recommendations in a txt file.
    """

    def __init__(self, parent, controller):

        # constructor to bulid the label, listbox, button in the Search page in GUI

        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Please choose your ", font=("Verdana", 20), anchor='w')
        label1.pack(pady=100,padx=100)
        w = tk.Listbox(self, font = 15)
        w.pack()
        w.insert(1, 'Tight schedule')
        w.insert(2, 'Flexible schedule')

        button1 = tk.Button(self, text="Bulid your travel plan...",
                            command=lambda: self.check_click2(w))
        button1.pack(side = LEFT, pady=10,padx=50) 

        button2 = tk.Button(self, text="Back to previous page",
                            command=lambda: controller.show_frame(Plan_secondPage, 0, 0))
        button2.pack(side = LEFT, pady=20,padx=50)  

        button3 = tk.Button(self, text="Back to home page",
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
            elif w.get(w.curselection()) == 'Tight schedule':     
                trip_planer(Time, Bugdet, 2)
            elif w.get(w.curselection()) == 'Flexible schedule':                         
                trip_planer(Time, Bugdet, 1)  
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")        

class Overview(tk.Frame):   
    
    """ 
    This class builds the frame 'Overview' to let users overview the informaiton from 'Restaurant', 'hotel', 'museum', 'attraction', and plot 
    our analysis into heatmap, histogram, and boxplot
    """

    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Overview!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)   
        
        w = tk.Listbox(self)

        w.insert(1, 'Hotel')
        w.insert(2, 'Restaurant')
        w.insert(3, 'Attractions')
        w.insert(4, 'Museums')
        w.pack(pady=50,padx=100, anchor = CENTER)

        button1 = tk.Button(self, text="Show the heatmap", width = 20,
                            command = lambda: self.check_click4(w))

        button1.pack(pady=10,padx=20) 
        
        button3 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button3.pack(pady=10,padx=20) 

    def check_click4(self, w):
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
                       
            if w.get(w.curselection()) == 'Hotel': 
                heatmap_creator('hotels')
            elif w.get(w.curselection()) == 'Restaurant':
                heatmap_creator('restaurants')
            elif w.get(w.cursselection()) == 'Attractions':
                heatmap_creator('attractions')
            elif w.get(w.curselection()) == 'Museums':
                heatmap_creator('museums')    
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")  

class Restaurant(tk.Frame):
    """ 
    This class builds the frame to 'Restaurant' let users choose the food category they want to know, 
    and then we will analyze our dataset and choose ten nearest and best restaurants for users via showing 
    a pdf file with reder chart and plot their locations in the map.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Restaurants!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose the category of the restaurant you want to search, then click 'search'", font=("Verdana", 16), anchor='w')
        label1.pack(pady=40,padx=40)

        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Chinese')
        w.insert(2, 'Japanese')
        w.insert(3, 'Asian')
        w.insert(4, 'Italian')
        w.insert(5, 'French')
        w.insert(6, 'US')    
        w.insert(7, 'European')
        w.insert(8, 'LatinAmerican')
        w.insert(9, 'Cafe_bar')
        w.insert(10, 'African')
        w.insert(11, 'MiddleEa')
        w.insert(12, 'Other')  

        p = Page_creator()

        button1 = tk.Button(self, text="Show the map", width = 10,
                            command=lambda: self.check_botton1(w))

        button1.pack(side = LEFT, pady=20,padx=60)

        button2 = tk.Button(self, text="Show the recommendations", width = 20, anchor=CENTER,
                            command = lambda: self.check_botton2(w))

        button2.pack(side = LEFT, pady=20,padx=60)

        button3 = tk.Button(self, text="Back to Search", width = 10,
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
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Chinese')
            elif w.get(w.curselection()) == 'Japanese':
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Japanese')
            elif w.get(w.curselection()) == 'Asian':
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Asian')
            elif w.get(w.curselection()) == 'Italian':    
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Italian')
            elif w.get(w.curselection()) == 'French':
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'French')  
            elif w.get(w.curselection()) == 'US':                 
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'US')
            elif w.get(w.curselection()) == 'European':                
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'European')
            elif w.get(w.curselection()) == 'LatinAmerican':
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'LatinAmerican')
            elif w.get(w.curselection()) == 'Cafe_bar':                
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Cafe_bar')
            elif w.get(w.curselection()) == 'African':                
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'African')
            elif w.get(w.curselection()) == 'MiddleEa':                
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'MiddleEa')
            elif w.get(w.curselection()) == 'Other':                
                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Other') 

        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")  

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
            elif w.get(w.curselection()) == 'US':                 
                p.Restaurant_page_creator(lat, logi, 'ctg', 'US')
            elif w.get(w.curselection()) == 'European':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'European')
            elif w.get(w.curselection()) == 'LatinAmerican':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'LatinAmerican')
            elif w.get(w.curselection()) == 'Cafe_bar':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Cafe_bar')
            elif w.get(w.curselection()) == 'African':
                p.Restaurant_page_creator(lat, logi, 'ctg', 'African')
            elif w.get(w.curselection()) == 'MiddleEa':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'MiddleEa')
            elif w.get(w.curselection()) == 'Other':                
                p.Restaurant_page_creator(lat, logi, 'ctg', 'Other') 

        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")

class Hotel(tk.Frame):
    """ 
    This class builds the frame to 'Hotel' let users choose the budget of hotels they want to spend, 
    and then we will analyze our dataset and choose ten nearest and best hotels for users via showing 
    a pdf file with reder chart and plot their locations in the map.
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hotel!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label1 = tk.Label(self, text="Please choose the price range of your hotel, then click 'search'", font=("Verdana", 16), anchor='w')
        label1.pack(pady=40,padx=40)

        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Economy hotel')
        w.insert(2, 'Commercial hotel')
        w.insert(3, 'Luxury hotel')

        p = Page_creator()

        button1 = tk.Button(self, text="Show the map", width = 10,
                            command=lambda: self.check_botton3(w))

        button1.pack(side = LEFT, pady=20,padx=60)

        button2 = tk.Button(self, text="Show the recommendations", width = 20,
                            command =
                            lambda: 
                                p.Hotel_page_creator(lat, logi, 'Price', 1)
                            if w.get(w.curselection()) == 'Economy hotel'           
                            else
                                p.Hotel_page_creator(lat, logi, 'Price', 2)
                            if w.get(w.curselection()) == 'Commercial hotel'
                            else 
                                p.Hotel_page_creator(lat, logi, 'Price', 3)
                            if w.get(w.curselection()) == 'Luxury hotel'
                            else 
                                print('haha'))
        
        button2.pack(side = LEFT, pady=20,padx=60)

        button3 = tk.Button(self, text="Back to Search", width = 10,
                            command=lambda: controller.show_frame(Search, 0, 0))
        button3.pack(side = LEFT, pady=20,padx=60)

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

            if w.get(w.curselection()) == 'Economy hotel':
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 1)
            elif w.get(w.curselection()) == 'Commercial hotel':                    
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 2)
            elif w.get(w.curselection()) == 'Luxury hotel':                
                p.plot_recommendations_for_hotels_in_map(lat, logi, 'Price', 3)
                              
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")
       
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

            if w.get(w.curselection()) == 'Economy hotel':
                p.Hotel_page_creator(lat, logi, 'Price', 1)
            if w.get(w.curselection()) == 'Commercial hotel':
                p.Hotel_page_creator(lat, logi, 'Price', 2)
            if w.get(w.curselection()) == 'Luxury hotel':                 
                p.Hotel_page_creator(lat, logi, 'Price', 3)
                      
        except IndexError:
            messagebox.showwarning("Error", "Please select one of the item in the listbox")

class Attractions(tk.Frame):
    """
    This class creates the frame 'Attraction' under the 'search' function. User can click the button 'show the recommendations'
    to see the recommendation information of attractions written in a rtf file. User also can click the button 'show the map' to 
    see the recommnedated attractions' name and address in a html file. 
    """
    def __init__(self, parent, controller):
        # constructor to bulid the label, listbox, button in the Search page in GUI
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Attractions!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        p = Page_creator()

        button1 = tk.Button(self, text="Show the recommendations",
                            command=lambda: p.Attraction_rtf_creator())
        button1.pack(pady=30,padx=20) 

        button2 = tk.Button(self, text="Show the map",
                            command=lambda: p.plot_recommendations_for_attractions_in_map())
        button2.pack(pady=30,padx=20)

        button3 = tk.Button(self, text="Back to Search",
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
        label = tk.Label(self, text="Museums!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        p = Page_creator()

        button1 = tk.Button(self, text="Show the recommendations",
                            command=lambda: p.Museum_rtf_creator())
        button1.pack(pady=30,padx=20) 

        button2 = tk.Button(self, text="Show the map",
                            command=lambda: p.plot_recommendations_for_museums_in_map())
        button2.pack(pady=30,padx=20)

        button3 = tk.Button(self, text="Back to Search",
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