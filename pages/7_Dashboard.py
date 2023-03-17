import streamlit as st 
import pandas as pd 
import sys
import os
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz
import plotly.express as px

def run_map_app():
       st.subheader("Static Map")

#layout ("centered" or "wide")
st.set_page_config(page_title='Dashboard',page_icon=":world_map:",layout='wide')
# sharing Variable amoung pages

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



st.header('Pattaya Flood Risk Dashboard')

empty1,content1,empty2,content2,empty3=st.columns([0.2,7,0.1,6,0.2])
with empty1:
        st.empty()
with content1:
    st.header("Pattaya_H3_Map")
    import streamlit as st
    import leafmap.kepler as leafmap
#12.886686,100.8527195
   
    m = leafmap.Map(center=[12.92, 100.86869255455714], zoom=11, widescreen=False)
    #in_csv=(r"C:\Users\Admin\OneDrive - Thammasat University\01_Thesis\11_ML_Model\H3_Predict.csv")
    in_csv ='https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/H3_MAP_Dataset_DEM2m_2016.csv'
    #m.add_csv(in_csv,layer_name="hex_data")
    #config=(r"./GIS_DATA\Atom.json")
    #m.add_csv(in_csv,layer_name="hex_data",config=config)
    configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mapconfig.json"
    config=configurl
    m.add_csv(in_csv,layer_name="hex_data",config=config) 
    m.to_streamlit()

    st.video('https://www.youtube.com/watch?v=ySZ97GSVb50')


with empty2:
        st.empty()
with content2:
    in_csv ='https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/H3_MAP_Dataset_DEM2m_2016.csv'
    df = pd.read_csv(in_csv)

    
  
    fig = px.histogram(data_frame=df,x='FloodRisk',color='FloodRisk', color_discrete_map={
                "ไม่มีความเสี่ยง": "#A6D96A",
                "เสี่ยงภัยปานกลาง": "#FDAE61",
                "เสี่ยงภัยมาก": "#D7191C",
                "เสี่ยงภัยน้อย": "#FFFFBF"
                },
             title="BarChart")
    fig.update(layout_showlegend=False)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    count1 = df["FloodRisk"].value_counts()
    dff = pd.DataFrame()
    palette={"ไม่มีความเสี่ยง": "#A6D96A","เสี่ยงภัยปานกลาง": "#FDAE61","เสี่ยงภัยมาก": "#D7191C","เสี่ยงภัยน้อย": "#FFFFBF"}
    dff["name"]=[str(i) for i in count1.index]
    dff["number"] = count1.values
    pie_fig=px.pie(dff, values="number", names="name",color=palette, hole=.6,title="PieChart")
    pie_fig.update(layout_showlegend=False)
    st.plotly_chart(pie_fig, theme="streamlit", use_container_width=True)







in_csv ='https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/H3_MAP_Dataset_DEM2m_2016.csv'
df = pd.read_csv(in_csv)
st.dataframe(df)