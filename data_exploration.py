import matplotlib
import pandas

datapath = './data/BFI_raw/bfi-weekend-box-office-report-2020-07-03-05.xls'
d = pandas.read_excel( datapath, skiprows = 1 )

print(d.columns)
print(d.dtypes)
#print (d)
print (d.head())
#print (d.tail())