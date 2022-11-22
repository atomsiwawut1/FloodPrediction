import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import leafmap.foliumap as leafmap
import geopandas
from geopandas import read_file

in_csv = 'https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv'
df = leafmap.csv_to_df(in_csv)

st.set_page_config(page_title='Home',layout='wide')
# sharing Variable amoung pages

# leafmap streamlit demo"
st.markdown('Source code: <https://github.com/giswqs/leafmap-streamlit/blob/master/app.py>')

"## Create a 3D map using Kepler.gl"
with st.echo():
    import streamlit as st
    import leafmap.kepler as leafmap

    m = leafmap.Map(center=[37.7621, -122.4143], zoom=12)
    in_csv = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_data.csv'
    config = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/hex_config.json'
    m.add_csv(in_csv, layer_name="hex_data", config=config)
    m.to_streamlit()


"## Create a heat map"
with st.echo():
    import leafmap.foliumap as leafmap

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    m = leafmap.Map(tiles='stamentoner')
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)
    m.to_streamlit(width=700, height=500, add_layer_control=True)
    


"## Load a GeoJSON file"
with st.echo():
    
    m = leafmap.Map(center=[0, 0], zoom=2)
    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines", info_mode='on_hover')
    m.to_streamlit()