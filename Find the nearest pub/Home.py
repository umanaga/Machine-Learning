
import streamlit as st
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import image
import os

st.title(':green[🍻 Welcome to Open Pub App 🍻]')


#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "pub.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "New_pub_Data.csv")

img = image.imread(IMAGE_PATH1)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.subheader(' Basic information of the pub dataset')


#df = pd.read_csv('New_pub_Data.csv')

st.markdown(f'Total number of pubs in the **United Kingdom**   **{df.shape[0]}** ')


choice = st.selectbox('',('Total columns','Head','Tail','unique local authority','null_values','Duplicate_values'))

if choice=='Total columns':
    st.markdown(f'Total columns in the data  **{df.columns}**')

elif choice=='Head':
    st.dataframe(df.head())

elif choice=='Tail':
    st.dataframe(df.tail())

elif choice=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in UK')

elif choice=='null_values':
    st.markdown('**There are no null values in our dataset**')
    st.text(df.isnull().sum())

elif choice=='Duplicate_values':
      st.markdown('**The number of duplicate values in our dataset**')
      st.text(df.duplicated().sum())

st.text('')
st.text('')


st.subheader(' Statistics information of the pub dataset')

st.dataframe(df.describe())




#subheader
st.write('By: :green[Uma Naga Silpa Bhupathiraju]')

