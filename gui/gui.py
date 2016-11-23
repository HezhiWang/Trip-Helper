import tkinter as tk
from tkinter import *
#from rader_chart import *
#from fibb import *]
import ex
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import pandas as pd
import page

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

        container = tk.Frame(self, width = 10000, height = 15000)

        container.pack(fill="both", expand = True)
        container.grid()
        container.config()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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

        button1.pack(side = LEFT, pady=20,padx=20)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(side = RIGHT, pady=20,padx=20) 

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

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage, 0, 0))
        button1.pack(pady=20,padx=20) 
        
class Restaurant(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Restaurants!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Search, 0, 0))
        button1.pack(pady=20,padx=20)

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

        button1 = tk.Button(self, text="Show", width = 20,
                            command =
                            lambda: 
                            page.page_creator(lat, logi, 'Price', 1)
                            if w.get(w.curselection()) == 'Economy hotel'           
                            else
                                page.page_creator(lat, logi, 'Price', 2)
                            if w.get(w.curselection()) == 'Commercial hotel'
                            else 
                                page.page_creator(lat, logi, 'Price', 3)
                            if w.get(w.curselection()) == 'Luxury hotel'
                            else 
                                print('haha'))
        #draw(lat, logi)
        button1.pack(side = LEFT, pady=10,padx=10)


        button2 = tk.Button(self, text="Back to Search", width = 20,
                            command=lambda: controller.show_frame(Search, 0, 0))
        button2.pack(side = RIGHT, pady=10,padx=10)

        
class Attractions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Attractions!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Search, 0, 0))
        button1.pack(pady=20,padx=20)

class Museums(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Museums!!!", font=("Verdana", 20))
        label.pack(pady=100,padx=100)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Search, 0, 0))
        button1.pack(pady=20,padx=20)


def main():
    
    app = Advisor()
    app.mainloop()

if __name__ == "__main__": main()

















