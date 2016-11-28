import pandas as pd
import numpy as np
import os

def rebuild(cur, fname):
    columns_name = ['Source', 'Location ID', 'Latitude', 'Longitude', 'Elevation', 'Year','Month','Day','Hour','Minute',
       'GHI (w/m2)', 'Temperature (c)', 'Relative Humidity (%)',
       'Solar Zenith Angle (Degree)', 'Wind Direction (Degree)',
       'Wind Speed (m/s)']
    df = pd.read_csv(cur + '/'+fname)
    co_val = df.ix[0][['Source','Location ID', 'Latitude','Longitude','Elevation']]
    df = df.drop(df.index[[0,1]])
    df3 = pd.DataFrame(df[['Source','Location ID','City','State','Country','Latitude','Longitude','Time Zone','Elevation','Local Time Zone','Clearsky DHI Units']].values, columns=columns_name[5:])
    df3['Source'] = co_val['Source']
    df3['Location ID'] = co_val['Location ID']
    df3['Latitude'] = co_val['Latitude']
    df3['Longitude'] = co_val['Longitude']
    df3['Elevation'] = co_val['Elevation']
    cols = df3.columns.tolist()
    cols = cols[-5:] + cols[:-5]
    df3 = df3[cols]
    if not os.path.exists(os.path.join('./data/', 'new_' + cur[4:])):
        os.makedirs(os.path.join('./data/', 'new_' + cur[4:]))
    folder_name = './data/new_'+ cur[4:]+'/'
    df3.to_csv(folder_name +'new_' + fname)
