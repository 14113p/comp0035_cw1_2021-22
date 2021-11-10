from numpy import NaN
import pandas
import os
import glob
import datetime

# get all the xls files in the folder
datapath = './data/BFI_raw/'
columns = ['Rank', 'Film', 'Weekend Gross', 'Weeks on release', 'Number of cinemas', 'Site average','Total Gross to date'] #columns to read

xls_files = glob.glob( os.path.join( datapath, "*.xls") )

#create an empty dataframe that will be output
d_main = pandas.DataFrame()

for a in xls_files:
    d_temp = pandas.read_excel( a, usecols=columns, skiprows = 1 )

    #drop lines starting with an empty cell (these are not film data)
    d_temp.dropna(subset = ['Rank','Film'], inplace = True)

    #merge it with the main one
    d_main = pandas.concat( [d_main, d_temp], ignore_index=True )

#drop the rank column, was needed only to recognise actual film info
d_main.drop( 'Rank', axis = 1, inplace = True )


####   tmdb API part    #####
#############################
import tmdbsimple as tmdb
tmdb.API_KEY = 'd9a2c308dbb2a7268990206ecf3028cf'
d_temp = pandas.DataFrame()
d_temp['API Genres'] = None
search = tmdb.Search()

for ind, row in d_main.iterrows():

    print( "Quering for entry " + str(ind + 1) + " out of " + str(len(d_main.index)) )

    search.movie( language='en', query = row['Film'] )

    #add genre, length, release date and rating
    if search.results:
        movie_object = tmdb.Movies( search.results[0]['id'] )
        movie_info = movie_object.info()
        d_main.at[ind, 'API Title'] = movie_info['title']
        d_main.at[ind, 'API length'] = movie_info['runtime']        
        if movie_info['vote_count'] > 5: d_main.at[ind, 'API Rating'] = movie_info['vote_average'] 
        if movie_info['budget'] != 0: d_main.at[ind, 'API Budget'] = movie_info['budget']
        d_main.at[ind, 'API Release Date'] = movie_info['release_date']
        genres = []
        for i in movie_info['genres']:
                genres.append( i['name'] )
        d_temp.loc[ind, 'API Genres'] = genres

# 
d_main = pandas.concat( [d_main, d_temp], axis=1, join='inner')

#drop films not found by the API and ones released before 2016(either rescreenings or misassigned by the API)
#print( d_main[ d_main['API Title'].isnull() ] )    # <== Proof

d_main.dropna(subset = ['API Title'], inplace = True)
d_main = d_main.loc[ d_main['API Title'] == d_main['Film'] ]
d_main['API Release Date'] = pandas.to_datetime(d_main['API Release Date'])
d_main = d_main.loc[ d_main['API Release Date'].dt.year >= 2016 ]

#export one xlsx file (newer format)
d_main.to_excel( excel_writer = 'data/BFI_merged.xlsx' )