import pandas
import os
import glob

# get all the xls files in the folder
datapath = './data/BFI_raw/'
path = os.getcwd()
xls_files = glob.glob( os.path.join( datapath, "*.xls") )

#import xls to dataframe (skip first row)
d_main = pandas.read_excel( datapath, skiprows = 1 )

for a in xls_files:
    d_temp = pandas.read_excel( a, skiprows = 1 )

#repeat for all the other files

##########################
#remove lines with NaN in first column

#remove lines whre title cannot be found by the API

#remove premieres older than 112 weeks

###########################

#    merge files into one

##########################
#add genre, length and ...