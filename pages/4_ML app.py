import streamlit as st 
import pandas as pd 
import leafmap
import folium
import leafmap.foliumap as leafmap
import geopandas as gpd
import xyzservices.providers as xyz
import sys
import os
import joblib
import streamlit as st
import leafmap.kepler as leafmap
from io import BytesIO
import pickle
import requests
from io import BytesIO
import pickle
import requests

st.set_page_config(page_title='Flood Risk MAP BY ML',page_icon=":robot_face:",layout='centered')
css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload .csv, .xlsx files not exceeding 100 MB")

def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024**2)
    return size_mb

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext in ('.csv','.xlsx'):
        return ext
    else:
        return False

def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model


if uploaded_file is not None:
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= 100:
            if ext == '.csv':
                # time being let load csv
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)
                st.header("Pattaya_H3 Map")

                import streamlit as st
                import leafmap.kepler as leafmap
                #12.886686,100.8527195

                m = leafmap.Map(center=[12.920912, 100.900474], zoom=11, widescreen=True)        
                #config=(r"./GIS_DATA\mlconfig.json")
                configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mlconfig.json"        
                config=configurl  
                m.add_df(df,layer_name="hex_data",config=config) 
                m.to_streamlit()
                for i, x in df.iterrows():
                    if df.loc[i,'LUL1_CODE'] =='U':
                         df.loc[i,'LU_Score'] = 4
                    elif df.loc[i,'LUL1_CODE']=='A':
                        df.loc[i,'LU_Score'] = 3
                    elif df.loc[i,'LUL1_CODE'] =='U':
                        df.loc[i,'LU_Score'] = 2
                    elif df.loc[i,'LUL1_CODE'] =='M':
                        df.loc[i,'LU_Score'] = 2
                    elif df.loc[i,'LUL1_CODE']=='F':
                        df.loc[i,'LU_Score'] = 1
                    else: 
                        df.loc[i,'LU_Score'] = 0
                #st.dataframe(df)
                feature_col=['Elevation','TotalRainfall','Slope','LengthFromRiver','LU_Score']
                df.dropna(inplace=True)
                X=df[feature_col]
                y=df.Risk_Score 
                #loadmodel = joblib.load("./GIS_DATA\Flood Hazard Map.joblib")
                #loadmodel = joblib.load("GIS_DATA\Flood Hazard Map.joblib")
                mLink = 'https://github.com/atomsiwawut1/FloodPrediction/blob/main/GIS_DATA/FloodModel.pkl?raw=true'
                mfile = BytesIO(requests.get(mLink).content)
                loadmodel=joblib.load(mfile)

                #MLmodel="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/453a18c6d71b18d9b0dd55c62a8a95a489aeb557/GIS_DATA/Flood%20Hazard%20Map.joblib"
                #loadmodel = joblib.load(MLmodel)
                


                predictEX= loadmodel.predict(X)
                my_array=predictEX
                
                df1 = pd.DataFrame(my_array, columns = ['Predicted Score'])

                df['Predicted Score'] =df1['Predicted Score']
                df['Predicted Score']=df['Predicted Score'].round(decimals = 0)
                st.dataframe(df)
                ml = leafmap.Map(center=[12.920912, 100.900474], zoom=11, widescreen=True)
                configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mlconfig.json"        
                config=configurl
                #config=(r"C:\Users\Admin\Desktop\Streamlit\00_AtomApps\GIS_DATA\mlconfig.json")
                ml.add_df(df,layer_name="hex_data",config=config)
                st.header("Pattaya_H3_ML_Map") 
                ml.to_streamlit()



            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_tuple = tuple(xl_file.sheet_names)
                sheet_name = st.sidebar.selectbox('Select the sheet',sheet_tuple)
                df = xl_file.parse(sheet_name)
                st.dataframe(df)

                st.header("Pattaya_H3 Map")
                import streamlit as st
                import leafmap.kepler as leafmap
                #12.886686,100.8527195
                m = leafmap.Map(center=[12.920912, 100.900474], zoom=11, widescreen=True)        
                #config=(r"./GIS_DATA\mlconfig.json")
                configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mlconfig.json"        
                config=configurl  
                m.add_df(df,layer_name="hex_data",config=config) 
                m.to_streamlit()
                for i, x in df.iterrows():
                    if df.loc[i,'LUL1_CODE'] =='U':
                         df.loc[i,'LU_Score'] = 4
                    elif df.loc[i,'LUL1_CODE']=='A':
                        df.loc[i,'LU_Score'] = 3
                    elif df.loc[i,'LUL1_CODE'] =='W':
                        df.loc[i,'LU_Score'] = 2
                    elif df.loc[i,'LUL1_CODE'] =='M':
                        df.loc[i,'LU_Score'] = 2
                    elif df.loc[i,'LUL1_CODE']=='F':
                        df.loc[i,'LU_Score'] = 1
                    else: 
                        df.loc[i,'LU_Score'] = 0
                #st.dataframe(df)
                df.dropna(inplace=True)
                feature_col=['Elevation','TotalRainfall','Slope','LengthFromRiver','LU_Score']
                X=df[feature_col]
                y=df.Risk_Score 
                #loadmodel = joblib.load("./GIS_DATA\Flood Hazard Map.joblib")
                #loadmodel = joblib.load("GIS_DATA\Flood Hazard Map.joblib")
                mLink = 'https://github.com/atomsiwawut1/FloodPrediction/blob/main/GIS_DATA/FloodModel.pkl?raw=true'
                mfile = BytesIO(requests.get(mLink).content)
                loadmodel=joblib.load(mfile)
                predictEX= loadmodel.predict(X)
                my_array=predictEX
                df1 = pd.DataFrame(my_array, columns = ['Predicted Score'])
                df['Predicted Score'] =df1['Predicted Score']
                df['Predicted Score']=df['Predicted Score'].round(decimals = 0)
                st.dataframe(df)

                ml = leafmap.Map(center=[12.920912, 100.900474], zoom=11, widescreen=True)
                configurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/GIS_DATA/mlconfig.json"        
                config=configurl        
                #config=(r"./GIS_DATA\mlconfig.json")
                ml.add_df(df,layer_name="hex_data",config=config) 
                ml.to_streamlit()


              
#The link needs to be the "raw" version (put raw.githubusercontent instead of github.com) and remove the "/blob/" portion of it.

#https://github.com/atomsiwawut1/FloodPrediction/blob/453a18c6d71b18d9b0dd55c62a8a95a489aeb557/GIS_DATA/Flood%20Hazard%20Map.joblib

#https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/453a18c6d71b18d9b0dd55c62a8a95a489aeb557/GIS_DATA/Flood%20Hazard%20Map.joblib

#Using the BytesIO you create a file object out of the response that you get from GitHub. That object can then be using in pickle.load. Note that I have added ?raw=true to the URL of the request.






