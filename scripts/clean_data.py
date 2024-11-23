import geopandas as gpd
import pandas as pd

data = gpd.read_file('../data/raw_data/raw_data.geojson')
data = data[['OCEANS', 'SAMPMETHOD', 'MEASUREMEN', 'UNIT', 'Latitude', 'Longitude', 'Date', 'geometry']]
data = data.rename(columns = {'MEASUREMEN' : 'Measurement', 'OCEANS': 'Ocean'})
data = data[data['UNIT'] == 'pieces/m3']
data.to_csv('../data/clean_data/clean_data.csv')