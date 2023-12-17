import pandas as pd
import streamlit as st
#import plotly.express as px
#from PIL import Image

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 20221')
st.subheader('was the tutorial helpful?')

for i in iris.sepal_length:
  st.subheader(i)
