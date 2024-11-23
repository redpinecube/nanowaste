import geopandas as gpd
import pandas as pd

data = gpd.read_file('../data/raw_data/raw_data.geojson')
data = data[data['SAMPMETHOD'] == 'Neuston net']
data = data[['OCEANS', 'MEASUREMEN', 'Latitude', 'Longitude', 'Date', 'geometry']]
data = data.rename(columns = {'MEASUREMEN' : 'Measurement', 'OCEANS': 'Ocean'})
data.to_csv('../data/clean_data/clean_data.csv')