import pandas as pd
import numpy as np

Chinese = ['Shanghainese','Taiwanese','HotPot','Chinese','Szechuan','DimSum','Cantonese']
Japanese = ['Japanese','SushiBars','Izakaya','Ramen']
Asian = ['Filipino','Indian','Thai','Cambodian','AsianFusion','Korean',
            'Vietnamese','Thai','Himalayan/Nepalese','Malaysian','SriLankan','Pakistani'
        ,'Bangladeshi']
Italian = ['Italian','Pizza']
French = ['French','Creperies']
US = ['American','Steakhouses','American(New)','Sandwiches',
            'American(Traditional)','Breakfast&Brunch','Salad','Burgers','Southern',
            'HotDogs','Breakfast&Brunch','Barbeque','FastFood',
              'ChickenWings','Cajun/Creole','Hawaiian']         
European = ['Greek','Mediterranean','British','ModernEuropean','Russian','German','Basque'
            ,'Tuscan', 'Polish','Belgian','Ukrainian','Irish','Austrian','Australian']
LatinAmerican = ['Mexican','LatinAmerican','Peruvian','Brazilian','Venezuelan', 'Colombian','Cuban'
            ,'Argentine','Tapas/SmallPlates','Salvadoran','Tacos','Empanadas','Dominican',
            'Caribbean','PuertoRican']
Cafe_bar = ['Cafes','Bars','Coffee&Tea','WineBars', 'CocktailBars','BeerBar','TeaRooms'
           ,'Gastropubs','Jazz&Blues','Pubs','DiveBars','SportsBars','Nightlife']
African = ['African','Moroccan','Egyptian','Kosher','Ethiopian']
MiddleEastern = ['MiddleEastern','Lebanese','Turkish','Afghan','Halal','Falafel','Persian/Iranian']
Other = ['Delis','SeafoodMarkets','BoatCharters', 'Venues&EventSpaces','Bookstores',
         'Bakeries','FoodStands','Bagels','MusicVenues','Desserts','Caterers', 
         'Lounges','Restaurants','SpecialtyFood', 'MeatShops', 'JuiceBars&Smoothies',
       'Fruits&Veggies', 'StreetVendors', 'FoodCourt','ComfortFood',
         'CheeseShops', 'Brasseries','FarmersMarket', 'Soup', 'Poutineries',
         'IceCream&FrozenYogurt', 'PerformingArts','OrganicStores', 
         'Fondue', 'Gluten-Free','Grocery', 'Poke', 'Butcher', 'Noodles', 'SoulFood', 'Buffets',
       'Cheesesteaks', 'ConvenienceStores','Tex-Mex', 'ChickenShop', 'Donuts',
       'CulturalCenter', 'ToyStores', 'LocalFlavor','Seafood',
       'CookingSchools','Food','Vegan','Vegetarian']

category = {'Chinese':Chinese,'Japanese':Japanese,'Asian':Asian,'Italian':Italian,
            'French':French, 'US':US, 'European':European, 'LatinAmerican':LatinAmerican,
            'Cafe_bar':Cafe_bar, 'African':African, 'MiddleEastern':MiddleEastern,
            'Other':Other}

yelp_data = pd.read_csv('yelp_data.csv',encoding = 'latin1')
d['first_category'] = d['category'].apply(lambda x: x.split(',')[0])

def categorize(x):
    for k,v in category.items():
        if x in v:
            return k
d['ctg'] = d['first_category'].apply(categorize)
d.drop(['first_category'], axis = 1)










