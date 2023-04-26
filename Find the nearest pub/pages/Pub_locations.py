import streamlit as st
import pandas as pd
import numpy as np
import os


#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH1 = os.path.join(dir_of_interest,"data", "New_pub_Data.csv")
df = pd.read_csv(DATA_PATH1)


# make header
st.header("Location of all Bars in United Kingdom")
# enter either postal code or local authority


location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
     location1 = st.selectbox("Select the Postal Code:", df['postcode'].unique())
     filtered_df = df[df['postcode'] == location1]
elif location_type == 'Local Authority':
     location2 = st.selectbox("Select the Postal Code:", df['local_authority'].unique())
     filtered_df = df[df['local_authority'] == location2]

if not filtered_df.empty:
    st.write("Number of Pubs in the area:", filtered_df.shape[0])

button_1 = st.button("Submit")
if button_1:
    st.text("Total Number of Pubs in this location is:")
    st.map(filtered_df)
    st.dataframe(filtered_df)
