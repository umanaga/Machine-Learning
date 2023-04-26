import streamlit as st
import pandas as pd
import numpy as np
import os


st.header("Find Nearest Pubs")


#Loading data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest, "data", "New_pub_Data.csv")
df = pd.read_csv(DATA_PATH1)

#input latitude and longitude from user

latitude=st.number_input(label="Enter Latitude Here")

longitude=st.number_input(label="Enter Longitude Here")


search_location=np.array((latitude,longitude))

original_location=np.array([df['latitude'],df['longitude']]).T

dist=np.sum((original_location-search_location)**2, axis=1)

df['Distance']=dist



df2=df.sort_values(by='Distance', ascending=True)[:5]

#List of Bar Names
st.subheader(f"Nearest five pubs for the Latitude and Longitube you entered:")

#Show Nearest Pubs on Map
st.map(data=df2, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(df2[['name','address','local_authority','postcode']])