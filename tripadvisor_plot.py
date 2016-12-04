def plot_review_density(df,filename):
    '''density plot of all reviews, filename == 'museum' or 'attraction' ''' 
    reviews = df[df['total_review']>=0]['total_review']
    mean = np.mean(reviews)
    std = np.std(reviews)
    median = np.median(reviews)
    ax1 = reviews.plot(kind='kde')
    ax1.set_xlim([0,max(reviews)])
    plt.xlabel('number of reviews')
    plt.ylabel('density')
    plt.title(filename+'_reviews_density_plot')
    plt.text(60000, 0.00010,'mean={:.2f} \n std={:.2f} \n median={:.2f}'.format(mean,std,median))
    plt.show()
    plt.savefig(filename+'_reviews_density.png')

def plot_rating_bar(df,filename):
    '''plot barplot of rating filename == 'museum' or 'attraction' '''
    rating = df[df['rating']!= -999]['rating']
    mean = np.mean(rating)
    std = np.std(rating)
    ax = rating.value_counts().plot(kind='bar')
    counts = ax.get_yticks()  
    tot = sum(count)
    ax.set_yticklabels(['{:2.1f}%'.format(x/tot*100) for x in counts])
    plt.xlabel('rating')
    plt.ylabel('ratio')
    plt.text(0.5, 0.5,'mean={:.2f}, std={:.2f}'.format(mean,std))
    plt.title(filename+' ratings')
    plt.show()
    plt.savefig(filename+'_ratings_bar.png')


