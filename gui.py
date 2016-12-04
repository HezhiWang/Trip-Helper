import tkinter as tk
from tkinter import *
#from rader_chart import *
#from fibb import *]
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import pandas as pd
from search import * 

"""
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure
"""

LARGE_FONT= ("Verdana", 12)
lat = 0
logi = 0

class Advisor(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, width = 20000, height = 15000)

        container.pack(fill="both", expand = True)
        #container.grid()
        #container.config()
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Restaurant, Hotel, Attractions, Museums, Search, Plan, Overview):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage, 0, 0)

    def show_frame(self, cont, lat, logi):

        frame = self.frames[cont]
        self.lat = lat
        self.logi = logi
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
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

class Search(tk.Frame):

    def __init__(self, parent, controller):
        root = tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to NYC", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        label = tk.Label(self, text="Please enter your location, then click 'Enter'", font=("Verdana", 16))
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
        #button = tk.Button(self, text = 'Sure', command = self.fetch(ents) )
        #button.pack(pady=20, padx=20)

        label3 = tk.Label(self, text="Please choose what you want to know, then click 'search'", font=("Verdana", 16), anchor='w')
        label3.pack(pady=20,padx=20)
        w = tk.Listbox(self)
        w.pack()
        w.insert(1, 'Restaurant')
        w.insert(2, 'Hotel')
        w.insert(3, 'Attractions')
        w.insert(4, 'Museums')
 
        button1 = tk.Button(self, text="Search",
                            command= 
                            #self.button_command(w.get(w.curselection())))

                            lambda: controller.show_frame(Restaurant, lat, logi) 
                            if w.get(w.curselection()) == 'Restaurant'           
                            else
                                controller.show_frame(Hotel, lat, logi)
                            if w.get(w.curselection()) == 'Hotel'
                            else 
                                controller.show_frame(Attractions, lat, logi)
                            if w.get(w.curselection()) == 'Attractions'
                            else
                                controller.show_frame(Museums, lat, logi))

        button1.pack(side = LEFT, pady=20,padx=70)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(side = RIGHT, pady=20,padx = 70) 

    def fetch(self, entries):
        global lat 
        lat = entries[0].get()
        global logi 
        logi = entries[1].get()

class Plan(tk.Frame):     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bulid you plan!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(pady=20,padx=20)  

class Overview(tk.Frame):     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Overview!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)   
        
        w = tk.Listbox(self)

        w.insert(1, 'Hotel')
        w.insert(2, 'Restaurant')
        w.insert(3, 'Attractions')
        w.insert(4, 'Museums')
        w.pack(pady=50,padx=100, anchor = CENTER)


        p = Page_creator()

        button1 = tk.Button(self, text="Show the heatmap", width = 20,
                            command =
                            lambda: 
                                p.heatmap_creator('hotels')
                            if w.get(w.curselection()) == 'Hotel'           
                            else
                                p.heatmap_creator('Restaurant')
                            if w.get(w.curselection()) == 'Restaurant'
                            else 
                                p.heatmap_creator('Attractions')
                            if w.get(w.curselection()) == 'Attractions'
                            else 
                                p.heatmap_creator('Museums')
                            if w.get(w.curselection()) == 'Museums'
                            else
                                print('haha'))

        button1.pack(pady=10,padx=20) 
        
        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button2.pack(pady=10,padx=20) 
        
class Restaurant(tk.Frame):

    def __init__(self, parent, controller):
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
                            command=lambda: 
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Chinese')
                            if w.get(w.curselection()) == 'Chinese'           
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Japanese')
                            if w.get(w.curselection()) == 'Japanese'
                            else 
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Asian')
                            if w.get(w.curselection()) == 'Asian'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Italian')
                            if w.get(w.curselection()) == 'Italian'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'French')  
                            if w.get(w.curselection()) == 'French' 
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'US')
                            if w.get(w.curselection()) == 'US'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'European')
                            if w.get(w.curselection()) == 'European'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'LatinAmerican')
                            if w.get(w.curselection()) == 'LatinAmerican'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Cafe_bar')
                            if w.get(w.curselection()) == 'Cafe_bar'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'African')
                            if w.get(w.curselection()) == 'African'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'MiddleEa')
                            if w.get(w.curselection()) == 'MiddleEa'
                            else
                                p.plot_recommendations_for_restaurants_in_map(lat, logi, 'ctg', 'Other') 
                            if w.get(w.curselection()) == 'Other'  
                            else 
                                print('haha'))

        button1.pack(side = LEFT, pady=20,padx=60)

        button2 = tk.Button(self, text="Show the recommendations", width = 20, anchor=CENTER,
                            command = lambda: 
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Chinese')
                            if w.get(w.curselection()) == 'Chinese'           
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Japanese')
                            if w.get(w.curselection()) == 'Japanese'
                            else 
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Asian')
                            if w.get(w.curselection()) == 'Asian'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Italian')
                            if w.get(w.curselection()) == 'Italian'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'French')  
                            if w.get(w.curselection()) == 'French' 
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'US')
                            if w.get(w.curselection()) == 'US'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'European')
                            if w.get(w.curselection()) == 'European'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'LatinAmerican')
                            if w.get(w.curselection()) == 'LatinAmerican'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Cafe_bar')
                            if w.get(w.curselection()) == 'Cafe_bar'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'African')
                            if w.get(w.curselection()) == 'African'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'MiddleEa')
                            if w.get(w.curselection()) == 'MiddleEa'
                            else
                                p.Restaurant_page_creator(lat, logi, 'ctg', 'Other') 
                            if w.get(w.curselection()) == 'Other'  
                            else 
                                print('haha'))

        button2.pack(side = LEFT, pady=20,padx=60)

        button3 = tk.Button(self, text="Back to Search", width = 10,
                            command=lambda: controller.show_frame(Search, 0, 0))

        button3.pack(side = LEFT, pady=20,padx=60)

class Hotel(tk.Frame):

    def __init__(self, parent, controller):
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
                            command=lambda: 
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Chinese')
                            if w.get(w.curselection()) == 'Chinese'           
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Japanese')
                            if w.get(w.curselection()) == 'Japanese'
                            else 
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Asian')
                            if w.get(w.curselection()) == 'Asian'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Italian')
                            if w.get(w.curselection()) == 'Italian'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'French')  
                            if w.get(w.curselection()) == 'French' 
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'US')
                            if w.get(w.curselection()) == 'US'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'European')
                            if w.get(w.curselection()) == 'European'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'LatinAmerican')
                            if w.get(w.curselection()) == 'LatinAmerican'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Cafe_bar')
                            if w.get(w.curselection()) == 'Cafe_bar'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'African')
                            if w.get(w.curselection()) == 'African'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'MiddleEa')
                            if w.get(w.curselection()) == 'MiddleEa'
                            else
                                p.plot_recommendations_for_hotels_in_map(lat, logi, 'ctg', 'Other') 
                            if w.get(w.curselection()) == 'Other'  
                            else 
                                print('haha'))

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
       
class Attractions(tk.Frame):

    def __init__(self, parent, controller):
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

    def __init__(self, parent, controller):
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
    
    app = Advisor()
    app.mainloop()

if __name__ == "__main__": main()

















