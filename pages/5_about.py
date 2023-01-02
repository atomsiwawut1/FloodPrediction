import streamlit as st 
import pandas as pd 
import sys
import os
st.set_page_config(page_title='About me',page_icon=":atom_symbol:",layout='wide')
about_variable = "from Main About.py Page"


#st.header('My CV', anchor=None)
#st.subheader("Siwawut Pattanasri")

css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.markdown("""


# My CV :notebook_with_decorative_cover: 

### Siwawut Pattanasri

##### Digital Solution Development

--- 

""")


empty1,content1,empty2,content2,empty3=st.columns([0.3,1.5,0.3,2,0.3])
with empty1:
        st.empty()
with content1:
        #st.write("here is the first column of content.")
        imageurl="https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/Media/Atom.png"
        #content1.image(".\Media\Atom.png",caption="Siwawut pattanasri",width=300)
        #content1.image(imageurl,caption="Siwawut pattanasri",width=300)
        content1.image(imageurl,caption="Siwawut pattanasri",use_column_width=True)


        st.markdown("""
### Qualifications and Professional Memberships
- ◉ Bachelor of Civil Engineering, Faculty of Engineering Thammasat University, Bangkok, Thailand

- ◉ License for Professional Practice Civil Engineer, Engineering Council of Thailand, Associate Engineer ID.272693

- ◉ Drone license (Thailand)

- ◉ Training certificate
    - ◎ ArchiStar Academy
        - ▹Dynamo Advanced
        - ▹Dynamo Designer
        - ▹Dynamo Essentials
        - ▹SketchUp Essentials
        - ▹Advanced VR in Unreal Engine 4

    - ◎ Linkedin learning
        - ▹Dynamo for Revit Python Scripting
        - ▹BIM 360 Design Essential Training

    - ◎ Google Analytics Academy
        - ▹Data Studio




        """)

with empty2:
        st.empty()
with content2:
        ##st.write("here is the second column of content.")
        st.markdown("""
        
➞      Siwawut has experiences in analysis and design structure of building with CSI software; 3D modelling with BIM software (SketchUp Revit Tekla Structures) management and planning of construction projects with Primavera P6 & Microsoft Project Data Visualization with Power BI and Data analysis with R & Python programming.

--- 
### EXPERTISE AND SKILLS
- ◉ Consulting about using BIM in project (i.e. BIM Model Development, Quantity Takeoff, Scheduling, Clash detection and Facility Management)
- ◉ Technical support for teams (Model management by Dynamo , Navisworks , ETC)
- ◉ 3D modeling with BIM software (Revit, Sketch up, Tekla structure, Rhino)
- ◉ 3D Visualization : D5 Render , Enscape
- ◉ Data analysis : R programing ,Python ,Excel ,Power BI ,Azure
- ◉ Research and stay informed on BIM related software and technologies.
- ◉ Drone flying skills : Drone Deploy ,Pix4d

---

### Management skills
- ◉ Information & Data Management : Monitor, manage and reviews project information and data.
- ◉ Scope & Change Control : Defines requirements and scope as key element of any project.
- ◉ Project Leadership : Focuses on strategy, manage details to align team and client towards project success.


### Relevant Experience
Whizdom101 Bangkok, Mixed-use Building; Project Commercial Phase II  (Feb 2019 – 2022), Magnolia Quality Development Corporation Limited | BIM Consultant

Terra, Data Center; Project Terra (Feb 2019 – 2021), ST Telemedia Limited | BIM Consultant

BIM Sansiri Corporate Service – Phase 1 | Bangkok | Sansiri Development High rise & Low Rise | 2019 – 2020 | BIM Corporate Consult

Dusit Central Park | Bangkok | Joint Venture of Dusit Thani with Central Pattana | 2019 - 2023 | BIM Management

Bangkok Cybertech District | Bangkok | Magnolia Quality Development Corporation Limited (MQDC) | 2020 - 2023 |BIM consultant

PATTAYA WORLDMARK | Chonburi | Magnolia Quality Development Corporation Limited (MQDC) | 2020 - 2025 | BIM Management

Pattaya Smart City Platform,Chonburi| EEC Phase 1  | 2021 - 2025 |Urban Development





        """)

with empty3:
        st.empty()




st.markdown("""

---

""")




empty1,content1,empty2,content2,empty3=st.columns([0.3,1.5,0.3,2,0.3])
with empty1:
        st.empty()
with content1:
        imageurl2 = "https://raw.githubusercontent.com/atomsiwawut1/FloodPrediction/main/Media/City.png"
        #st.image(".\Media\City.png",caption="https://www.facebook.com/siwawut.pattanasri/",width=600)
        #st.image(imageurl2,caption="https://www.facebook.com/siwawut.pattanasri/",width=600)
        st.image(imageurl2,caption="https://www.facebook.com/siwawut.pattanasri/",use_column_width=True)
        #st.image('hackershrine.jpg',use_column_width=True)
with empty2:
        st.empty()
with content2:
        st.markdown("""

## contract

[Facebook](https://www.facebook.com/siwawut.pattanasri/)


lineID : atomsiwawut

:e-mail: atomsiwawut@gmail.com

:telephone_receiver: 0828952663

""")
with empty3:
        st.empty()







