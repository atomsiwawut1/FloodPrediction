import streamlit as st 
import pandas as pd 

import sys
import os
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz

def run_map_app():
   st.subheader("Static Map")

#layout ("centered" or "wide")
st.set_page_config(page_title='Map',page_icon="🧊",layout='centered')
# sharing Variable amoung pages


st.subheader("Map")

tab1, tab2, tab3 ,tab4 ,tab5 ,tab6 = st.tabs(["2D Map", "3D Map", "Compare","CSV","SH","Test"])

with tab1:
   st.header("2D Map")
   import leafmap.foliumap as leafmap
   filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
   m = leafmap.Map(tiles='stamentoner')
   m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
   m.to_streamlit(width=700, height=500, add_layer_control=True)



with tab2:
   st.header("3D Map")
   import streamlit as st
   import leafmap.kepler as leafmap

   m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
   in_csv = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_data.csv'
   config = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_config.json'
   m.add_csv(in_csv, layer_name="hex_data", config=config)
   m.to_streamlit(width=700, height=500, add_layer_control=True)

with tab3:
   import folium
   import leafmap.foliumap as leafmap
   m = leafmap.Map(center=[40, -100], zoom=4)

   url1 = 'https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2001_Land_Cover_L48/wms?'
   url2 = 'https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms?'

   left_layer = folium.WmsTileLayer(
      url=url1,
      layers='NLCD_2001_Land_Cover_L48',
      name='NLCD 2001',
      attr='MRLC',
      fmt="image/png",
      transparent=True,
)
   right_layer = folium.WmsTileLayer(
      url=url2,
      layers='NLCD_2019_Land_Cover_L48',
      name='NLCD 2019',
      attr='MRLC',
      fmt="image/png",
      transparent=True,
)

   m.split_map(left_layer, right_layer)
   m.to_streamlit()

with tab4:
   
   import geopandas as gpd
   gdf = gpd.read_file("https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.geojson")
   m = leafmap.Map(center=[20, 0], zoom=1)
   m.add_gdf(gdf, "World cities")
   m.to_streamlit()




with tab5:
   m = leafmap.Map(center=[20, 0], zoom=1)
   in_shp = "https://github.com/giswqs/leafmap/raw/master/examples/data/countries.zip"
   m.add_shp(in_shp, "Countries")
   m.to_streamlit()


with tab6:
   st.header("Pattaya_H3 Map")
   import streamlit as st
   import leafmap.kepler as leafmap
#12.886686,100.8527195
   m = leafmap.Map(center=[12.920912, 100.900474], zoom=11, widescreen=True)
   #in_csv=(r"GIS_DATA\CSV_H3_Edit.csv")
   in_csv="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/5e0114776b5883bccf428a9e54de502754a649ba/GIS_DATA/CSV_H3_ML.csv"
   configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mlconfig.json"        
   config=configurl        
   #config=(r"./GIS_DATA\mlconfig.json")
   m.add_df(in_csv,layer_name="hex_data",config=config) 
   m.to_streamlit()

  









   # button widget
   #st.subheader('SAVE CONFIG')
   #st.caption('')
   #if st.button('SAVE CONFIG'):
   #m.save_config("GIS_DATA/Atom111config.json")
   #st.write('save')


