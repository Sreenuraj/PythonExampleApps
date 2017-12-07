import folium
import pandas as pd


map = folium.Map(location = [48.7767982,-121.8109970], zoom_start = 6,tiles='Mapbox bright')

fgv = folium.FeatureGroup('Volcanoes')

data = pd.read_csv('Volcanoes_USA.txt')
#name = list(data['NAME'])
elv = list(data['ELEV'])
lat = list(data['LAT'])
lon = list(data['LON'])

def color_producer(elv):
    if elv > 3000:
        return '#8B0000'
    elif elv > 2000:
        return '#FF8C00'
    else:
        return '#006400'


for lt,lg,el in zip(lat,lon,elv):
    #print(lt,lg,n)
    fgv.add_child(folium.CircleMarker(location=[lt, lg],radius=5,fill_opacity=1,
    popup=str(el),fill=True, color=color_producer(el)))

fgp = folium.FeatureGroup('Population')
data_file = open('world.json',encoding='utf-8-sig')
fgp.add_child(folium.GeoJson(data=data_file.read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000 else 'red'} ))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('My_test_map.html')
