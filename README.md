# New York City Trip Helper

This is the final project for **DS-GA 1007 Programming for Data Science** .
## Contributors

Hezhi Wang [https://github.com/HezhiWang] (https://github.com/HezhiWang) Netid: hw1567

Han Zhao [https://github.com/hzhao16] (https://github.com/hzhao16) Netid: hz1411

Storm Avery Ross [https://github.com/sar516] (https://github.com/sar516) Netid: sar516

## Dependencies
- Python = 3.5
- tkinter == 8.5.18
- geopy == 1.11.0
- gmplot == 1.1.1
- seaborn == 0.7.1
- numpy == 1.11.1
- pandas == 0.18.1
- matplotlib == 1.5.3
- sklearn == 0.18.1

if any of the packages are missing, type in your command line(MAC OS X)
```sh
$ pip install <package>==<version>
```

## How to run

Switch to the directory of the application, and run on command line(MAC OS X):
```sh
$ python gui.py
```
## How to test
Switch to the directory of the application, and run on command line(MAC OS X):
```sh
$ python -m unittest discover
```

## How to use
This application allows users to,

1. **Search** for places of interest by entering their latitude and longitude and specify their preferences.

2. **Plan** a trip to NYC by selecting their preferred budget, time and schedule to access a customized trip plan including recommendations for attractions, restaurants and hotels.

3. **Overview** certain visualized stats about NYC attractions, museums, restaurants and hotels, including heat map, bar chart, pie chart etc.

For detailed description, please see below.

## Description

This program helps you to have fun in New York City. 

It consists of 3 main functions that you can select on Home Page - Search, Plan and Overview. Our datasets are scraped from [Booking.com](http://www.booking.com/) for hotels, [Tripadvisor.com](https://www.tripadvisor.com/) for attractions and museums, and [Yelp.com](https://www.yelp.com/nyc) for restaurants.

Firstly, You can “search” nearby locations that fall in 4 categories: restaurants, hotels, attractions and museums. You need to enter your current latitude and longitude, and select what kind of locations you are interested in. Your coordinate should be within NYC or an error message will be raised. We also have specific filters for certain locations. For restaurants, you can choose from 12 different categories, including Italian, Chinese, Cafe & bar etc. For hotels, you can choose from 3 price levels based on your budget. Our program will search for all nearby locations that satisfy your filter, and sort by their rating and number of reviews. To see our recommendations for you, you can click “show the map” to see them marked on a Google Map. If you prefer a written version, simply click “show the recommendations”, and a PDF file will be generated under “Results” folder. It contains the name of each recommended locations, each with a radar chart showing their ratings from different angles. You can always go back to the search main page by “Back to Search”.

Second, you can “plan” a trip to New York. Just choose how many days you want to stay (from 1 day to 7 days) , how much money you could spend, and how you would arrange your time (whether you prefer a tight schedule to see as many as places of interest as possible, or you like to be more flexible and just enjoy yourself). You can reset your choice by clicking “Back to previous page”. And finally, click “Build your travel plan”. Et voilà! Now you can see your travel plan under “Results” folder in rtf format. You will see our arrangement for your each day, including attractions and museums to visit, and recommendations of hotels and restaurants. Our algorithm utilizes sorting, clustering(revised K-means algorithm that return K clusters with the same number of elements) by distance and permutation, so you can have incredible amount of different plans, each highlights most loved travel spots, and you won’t waste too much time on traffic. You can click “Back to previous page” to reset your preference and get a whole new plan.

And finally, we also provide an “overview” section. Here you can have a look at our visualizations of overall stats of New York restaurants, hotels, attractions and museums. Just select a type and click “Show plots”. Then on next page you can select what kind of plot you would like to see. We have heatmap on Google map, density plot for reviews, pie plot by price or category, bar plot for ratings as well as mean, variance and median. On clicking the relevant button, a figure will pop up and also be saved to Results folder. 

Enjoy your trip in New York!

