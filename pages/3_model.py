#--------------------------
#IMPORT LIBRARIES
#import streamlit
import streamlit as st
#specklepy libraries
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_account_from_token
#import pandas
import pandas as pd
#import plotly express
import plotly.express as px
#--------------------------

#--------------------------
#PAGE CONFIG
st.set_page_config(
    page_title="Speckle Test",
    page_icon="๐"
)
#--------------------------
css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#--------------------------
#CONTAINERS
header = st.container()
input = st.container()
viewer = st.container()
report = st.container()
graphs = st.container()
#--------------------------

#HEADER
#Page Header
with header:
    st.title("Speckle Test Model")
#About info
with header.expander("About this app๐ฝ", expanded=True):
    st.markdown(
        """ test
        """
    )
#--------------------------


with input:
    st.subheader("Inputs")

    #-------
    #Columns for inputs
    serverCol, tokenCol = st.columns([1,3])
    #-------

     #-------
	#User Input boxes
    speckleServer = serverCol.text_input("Server URL", "speckle.xyz", help="Speckle server to connect.")
 
    speckleToken=st.secrets["speckleToken"]

    #CLIENT
    client = SpeckleClient(host=speckleServer)
    #Get account from Token
    account = get_account_from_token(speckleToken, speckleServer)
    #Authenticate
    client.authenticate_with_account(account)
    #-------
    #-------
    #Streams List๐
    streams = client.stream.list()
    #Get Stream Names
    streamNames = [s.name for s in streams]
    #Dropdown for stream selection
    sName = st.selectbox(label="Select your stream", options=streamNames, help="Select your stream from the dropdown")

    #SELECTED STREAM โ
    stream = client.stream.search(sName)[0]

    #Stream Branches ๐ด
    branches = client.branch.list(stream.id)
    #Stream Commits ๐น
    commits = client.commit.list(stream.id, limit=100)
    #-------
def commit2viewer(stream, commit, height=400) -> str:
    embed_src = "<https://speckle.xyz/embed?stream="+stream.id+"&commit=>"+commit.id
    return st.components.v1.iframe(src=embed_src, height=height)

with viewer:
    st.subheader("Revit Model๐")
    commit2viewer(stream, commits[0])
    st.components.v1.iframe(src="https://speckle.xyz/embed?stream=6a645d341a&commit=36162589e0",width=800,height=1000)
















