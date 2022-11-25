import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import leafmap.foliumap as leafmap
import geopandas
from geopandas import read_file

st.set_page_config(page_title='Home',page_icon="🧊",layout='centered')



st.header('My Hobby')
image_url="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/Media/hunt.jpg"
st.image(image_url,caption="best survival game",width=500)

st.header('ปรับปรุงริมน้ำตลาดท่านา')
st.image("Media\TANA.png",caption="best survival game",width=500)


st.header('ปรับปรุงริมน้ำตลาดท่านา')
st.image("Media\TANA2.png",caption="best survival game",width=500)