import folium
import pandas as pd

# Create the folium.map object
map = folium.Map(location = [48.7767982,-122.8109970], zoom_start = 6,tiles='Mapbox bright')

# Reading the file which has the Volcanoes data in the same dir
data = pd.read_csv('Volcanoes_USA.txt')
# Creating a list obj for elevation, lat and log
elv = list(data['ELEV'])
lat = list(data['LAT'])
lon = list(data['LON'])

# function which gives color as output
def color_producer(elv):
    if elv > 3000:
        return '#8B0000'
    elif elv > 2000:
        return '#FF8C00'
    else:
        return '#006400'

# A folium FeatureGroup will help to organize the layer we add as add_child
fgv = folium.FeatureGroup('Volcanoes')
# Using a for loop for iterating through the list and adding the same to the map
for lt,lg,el in zip(lat,lon,elv):
    # add_child to add layers
    fgv.add_child(folium.CircleMarker(location=[lt, lg],radius=5,fill_opacity=1,
    popup=str(el),fill=True, color=color_producer(el)))

# a new FeatureGroup for population
fgp = folium.FeatureGroup('Population')
data_file = open('world.json',encoding='utf-8-sig')
# using GeoJson we can read a geojson file and manupilate
fgp.add_child(folium.GeoJson(data=data_file.read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000 else 'red'} ))

# Adding the FeatureGroups to the map object
map.add_child(fgv)
map.add_child(fgp)
# folium.LayerControl to control the layers
map.add_child(folium.LayerControl())
# with map.save we will create the map html
map.save('My_test_map.html')
