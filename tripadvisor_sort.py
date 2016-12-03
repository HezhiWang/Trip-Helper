def sort_trip(df):
    '''for museums/attractions with ratings higher than 3.5 and total number of reviews 
    more than 1000, sort by rating and total reviews both descending.
    '''
    mask1 = df['rating']>=3.5
    mask2 = df['total_review']>=1000
    mask = pd.concat((mask1, mask2), axis=1)
    ind_sub = mask.all(axis=1)
    df_sub = df.ix[ind_sub]
    df_sorted = df_sub.sort_values(by=['rating','total_review'],ascending=[False,False])
    return df_sorted

def print_to_rtf(df, filename):
    '''print sorted museums/attractions to rtf file ,filename =='museum' or 'attraction' '''
    
    # replace - "-999" -> "NA"
    df = df.replace(to_replace= '-999', value='N.A.')
    # open file
    rtf = open(filename+'.rtf', 'w')
    # header info
    rtf.write(r'{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fswiss\fcharset0 Arial;}}')
    for i in range(df.shape[0]):
        rtf.write(r'\ \b {} \b0 \line \ \b Rating:\b0 {} \t \b Reviews:\b0 {} \line'.format(df['name'].iloc[i],
               df['rating'].iloc[i], df['total_review'].iloc[i]))
        rtf.write(r'\ \b Details: \b0 {} \line\ \b Description: \b0 {} \line'.format(df['detail'].iloc[i],
                                                                    df['description'].iloc[i]))
        rtf.write(r'\line')
    rtf.write(r'}\n\x00')
    rtf.close()


def generate_combined_dataset(d1,d2):
    '''This is to generate a combined and sorted dataset of museums and attractions for trip planning'''
    combined_df = pd.concat([d1,d2],ignore_index=True)
    combined_df = combined_df.drop_duplicates(subset=['name'],keep='first')
    combined_df = sort_trip(combined_df).reset_index(drop=True)
    return combined_df




