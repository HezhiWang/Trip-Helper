def plot_review_density(df,filename):
    '''
    This function to density plot of all reviews, filename == 'museum', 'attraction', 'restaurant', 'hotel'.

    Parameters:
        df: Dataframe
        filename: string
    ''' 
    reviews = df[df['Total_review']>=0]['Total_review']
    mean = np.mean(reviews)
    std = np.std(reviews)
    median = np.median(reviews)
    ax1 = reviews.plot(kind='kde')
    ax1.set_xlim([0,max(reviews)])
    plt.xlabel('number of reviews')
    plt.ylabel('density')
    plt.title(filename + '_reviews_density_plot')
    plt.text(60000, 0.00010,'mean={:.2f} \n std={:.2f} \n median={:.2f}'.format(mean,std,median))
    plt.show()
    path = os.path.abspath('Results')
    plt.savefig(path + '/' + filename + '_reviews_density.png')

def plot_rating_bar(df,filename):
    '''
    This function to plot barplot of rating filename == 'museum', 'attraction', 'restaurant', 'hotel'. 

    Parameters:
        df: Dataframe
        filename: string 
    '''
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
    path = os.path.abspath('Results')
    plt.savefig(path + '/' + filename + '_ratings_bar.png')

def price_transform(price):
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
    elif (filename == 'restaurant'):
        df = self.restaurant
        yelp_category(df)        

    value_column = ['Avgscore', 'Cleanliness', 'Comfort', 'Facilities', 'Free Wifi', 'Location', 'Staff', 'Value for money']
    df_mean = df[value_column].groupby(df['category']).mean().T

    df_mean.plot(kind = 'bar', alpha = 0.7)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('Rating Category')
    plt.ylabel('Average')
    plt.title('Bar chart')        
