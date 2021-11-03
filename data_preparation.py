from numpy import NaN
import pandas
import os
import glob

# get all the xls files in the folder
datapath = './data/BFI_raw/'
columns = ['Rank', 'Film', 'Country of Origin', 'Weekend Gross', 'Weeks on release', 'Number of cinemas', 'Site average','Total Gross to date'] # <= these are columns to read, info from exploration

xls_files = glob.glob( os.path.join( datapath, "*.xls") )

#create an empty dataframe, import only column names
d_main = pandas.DataFrame()

for a in xls_files:
    #import another xls
    d_temp = pandas.read_excel( a, usecols=columns, skiprows = 1 )

    ########clean the file

    #drop lines starting with an empty cell

    #d_temp[ d_temp['Rank'] == NaN].drop(axis = 0)
    d_temp.dropna(subset = ['Rank','Film'], inplace = True)

    #merge it with the main one

    d_main = pandas.concat( [d_main, d_temp], ignore_index=True )

#drop the column added by concat and the rank column, was needed only to recognise actual film info

d_main.drop( 'Rank', axis = 1, inplace = True )

#remove premieres older than 112 (2 years) weeks, to exclude special screenings (these usually include only commercially succesful movies, what would skew the analysis)

#############################################################
####    tmdb   API part
#############################################################

import tmdbsimple as tmdb
tmdb.API_KEY = 'd9a2c308dbb2a7268990206ecf3028cf'
search = tmdb.Search()

for index, row in d_main.iterrows():

    print( "Quering for entry " + str(index + 1) + " out of " + str(len(d_main.index)) )

    search.movie( language='en', query = row['Film'] )

    if search.results:
        #add genre, length, release date and rating
        print( index )
        a = search.results[0]
        d_main.at[index, 'API Title'] = a['title']
        ################row['API length'] = a['runtime']
        ################d_main['API genres'] = a['genre_ids']
        #d_main.ix[index, 'API Rating'] = a['rating']

#drop films not found by the API (these are mostly  rescreenings anyway, as they have additional text, such as '(30th Anniversary)')
#print( d_main[ d_main['API Title'].isnull() ] )    # <== Proof

d_main.dropna(subset = ['API Title'], inplace = True)

##############################################################

#export one xlsx file (newer format)
d_main.to_excel( excel_writer = 'data/BFI_merged.xlsx' )