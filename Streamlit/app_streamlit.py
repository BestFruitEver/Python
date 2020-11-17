import streamlit as st
import pandas as pd

#Titre
st.title("Application")

@st.cache
def load_data(nrows):
    data = pd.read_csv("C:/Users/romai/Documents/Master/Python/UML/price_availability.csv", nrows=nrows)
    return data

df=load_data(15)
st.write(df)