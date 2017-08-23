# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 23:05:08 2017
This script contains a comprehensive example
of importing data from a CSV file.
Specific directions are given to pandas.read_csv
to not make the first line the header, to
assign proper column names and also the following:
    1. how to recode -1 values in the sunspot columns as missing
    2. How to combine the first 3 columns into a single date
    3. How to use the date as the index
    4. How to discard redundant columns
    
Also, the processed data frame is written to a csv file, 
a tsv file and an xlsx file.
"""

#import os
#print(os.getcwd())
#print(os.listdir()

import pandas as pd
col_names = ['year', 'month', 'day', 'dec_date', 'sun_spots',
             'definite']
fn = 'ISSN_D_tot.csv'
df = pd.read_csv(fn)
df.info()

print("-"*20)

df = pd.read_csv(fn, header = None, na_values ={"sun_spots":[' -1']}, parse_dates = [[0, 1, 2]], names = col_names)
print(df.iloc[10:20,])

df.info()

print("-"*20)

df.index = df['year_month_day'] #assign index; note that
#year_month_day column is retained
print(df.iloc[10:20,:])
df.info()

print("-"*20)

df = df[['sun_spots','definite']] #remove year_month_day
#and dec_date data columns, but retain year_month_day
#index

#Also, rename index to date

df.index.name = "date"
print(df.iloc[10:20])

"""
Now we'll write the dataframe to
a csv file, a tsv file and an xlsx file.
"""

out_csv = 'sunspots.csv'

out_tsv = 'sunspots.tsv'

out_xlsx = 'sunspots.xlsx'

df.to_csv(out_csv)

df.to_csv(out_tsv, sep = '\t')

df.to_excel(out_xlsx)






