
from Data.Read_data import *
from Sort.yelp_sort import *

class overview_plot:
    '''
    This class deals with plotting figures in overview section. 
    It reads our source data, plot barplot, piechart, densityplot on different conditions
    '''
    def __init__(self):
        hotel, restaurant, museum, attraction = Read_data()
        self.hotel = hotel
        self.restaurant = restaurant
        self.museum = museum
        self.attraction = attraction

    def plot_review_density(self, filename):
        '''density plot of reviews, filename == 'museum','attraction','restaurant','hotel' '''
        for df in [self.hotel, self.restaurant, self.museum, self.attraction]:
            reviews = df[df['Total_review']>=0]['Total_review']
            mean = np.mean(reviews)
            std = np.std(reviews)
            median = np.median(reviews)
            ax = reviews.plot(kind='kde')
            ax.set_xlim([0,max(reviews)])
            text = 'mean=%.2f \n std=%.2f \n median=%.2f'%(mean, std, median)
            ax.text(0.65, 0.95, text, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)
            plt.xlabel('number of reviews')
            plt.ylabel('density')
            plt.title(filename+'_reviews_density_plot')
            plt.savefig('Results/' + filename + '_reviews_density.png')
            plt.show()
            plt.close()

    def plot_rating_bar(self, filename):
        '''plot barplot of rating, filename == 'museum' or 'attraction','restaurant','hotel' '''
        for df in [self.hotel, self.restaurant, self.museum, self.attraction]:
            rating = df[df['Avgscore']!= -999]['Avgscore']
            mean = np.mean(rating)
            std = np.std(rating)
            ax = rating.value_counts().plot(kind='bar')
            counts = ax.get_yticks()  
            tot = sum(count)
            ax.set_yticklabels(['{:2.1f}%'.format(x/tot*100) for x in counts])
            plt.xlabel('rating')
            plt.ylabel('ratio')
            plt.text(0.5, 0.5,'mean={:.2f}, std={:.2f}'.format(mean,std))
            plt.title(filename + ' ratings')
            plt.show()
            plt.savefig('Results/' + filename + '_ratings_bar.png')
            plt.close()

    def plot_pie(self, filename):
        '''
        plot pie chart for 'restaurant' and 'hotel'
        if filename = 'restaurant', plot pie chart by category
        if filename = 'hotel', plot pie chart by price

        '''
        if filename == 'restaurant':
            yelp_category(self.restaurant)
            plt.figure(figsize=(8,8))
            self.restaurant['ctg'].value_counts().plot(kind='pie',autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Pie chart for restaurants by category')
            plt.savefig('../Results/pie_chart_' + filename + '.png')
            plt.show()
            plt.close()
        if filename == 'hotel':
            df = self.hotel
            df['category'] = df['Price'].apply(self.price_transform)
            df['category'].value_counts().plot(kind='pie',autopct='%1.1f%%')
            plt.axis('equal')
            plt.title('Pie chart for hotels by category')
            plt.savefig('../Results/pie_chart_' + filename + '.png')
            plt.show()
            plt.close()

    def price_transform(price):
        """
        This function tranform the parameter price to three categories: Economy hotel, Commercial hotel,
        Luxury hotel. 

        Parameter:
            price: int

        Return:
            String: Economy hotel, Commercial hotel, Luxury hotel. 
        """
        if (1 == price or 2 == price):
            return 'Economy hotel'
        elif (3 == price or 4 == price ):
            return 'Commercial hotel'
        elif (price == 5):
            return 'Luxury hotel'

    def plot_bar_chart(self, filename):
        if (filename == 'hotel'):
            df = self.hotel
            df['category'] = df['Price'].apply(price_transform)
            df = df[df['category'].notnull()]
            df = df[df['Avgscore'] != -999]

            value_column = ['Avgscore', 'Cleanliness', 'Comfort', 'Facilities', 'Free Wifi', 'Location', 'Staff', 'Value for money']
            df_mean = df[value_column].groupby(df['category']).mean().T

            df_mean.plot(kind = 'bar', alpha = 0.7)
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            plt.xlabel('Rating Category')
            plt.ylabel('Average')
            plt.title('Bar chart')  

            plt.show()        
            path = os.path.abspath('Results')
            plt.savefig(path + '/' + filename + '_rating_scores_bar.png')
            plt.close()

        elif (filename == 'restaurant'):
            df = self.restaurant
            yelp_category(df)  

            value_column = ['Total_review', 'Avgscore']
            df_mean = df[value_column].groupby(df['ctg']).mean()  

            f, axarr = plt.subplots(2, sharex=True)

            ind = np.arange(12)
            width = 0.35
            rects1 = axarr[0].bar(ind, df_mean['Total_review'], width, color='r', label = 'Total reviews')
            axarr[0].set_xticks(ind + width)
            axarr[0].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            axarr[0].set_xticklabels(('African', 'Asian', 'Cafe_bar', 'Chinese', 'European', 'French', 'Italian', 'Japanese', 'LatinAmerican', 'MiddleEastern', 'Other', 'US'), rotation = 'vertical')
            axarr[0].set_title('Restaurant Bar chart')

            rects2 = axarr[1].bar(ind, df_mean['Avgscore'], width, color='b', label = 'Average Score')
            axarr[1].set_xticks(ind + width)
            axarr[1].set_xticklabels(('African', 'Asian', 'Cafe_bar', 'Chinese'

            plt.show()
            path = os.path.abspath('Results')
            plt.savefig(path + '/' + filename + '_rating_scores_bar.png')    
            plt.close()

      
