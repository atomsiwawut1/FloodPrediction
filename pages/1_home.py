import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import leafmap.foliumap as leafmap
import geopandas
from geopandas import read_file

st.set_page_config(page_title='Home',page_icon=":derelict_house_building:",layout='centered')

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#st.header('My Hobby')
#image_url="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/Media/hunt.jpg"
#st.image(image_url,caption="best survival game",width=500)

st.header('ปรับปรุงริมน้ำตลาดท่านา')
st.image("Media/TANA.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)


st.subheader('โครงการพัฒนาพื้นที่ริมแม่น้ำนครชัยศรีเพื่อรองรับการท่องเที่ยว')
st.image("Media/TANA2.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)

st.subheader('โครงการก่อสร้างท่าเรือท่องเที่ยวตลาดท่านา ส่งเสริมเส้นทางล่องเรือชมวิถีชีวิตชุมชนริมแม่น้ำนครชัยศรี')
st.image("Media/TANA3.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)

st.subheader('โครงการปรับปรุงภูมิทัศน์บริเวณทางเข้าตลาดท่านา')
st.image("Media/TANA4.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)

st.subheader('โครงการพัฒนาเส้นทางจักรยานท่องเที่ยวชุมชนท่านาและพื้นที่เชื่อมโยง')
st.image("Media/TANA5.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)

st.subheader('โครงการปรับปรุงจุดรับ-ส่งรถโดยสารสาธารณะ')
st.image("Media/TANA6.png",caption="ปรับปรุงริมน้ำตลาดท่านา",width=500)