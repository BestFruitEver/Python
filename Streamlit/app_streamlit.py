from pathlib import Path
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Titre
st.title("Application")

@st.cache
def load_data():
    data = pd.read_csv("C:/Users/romai/Documents/Master/Python/Dataset/price_availability.csv", sep=";")
    return data

df=load_data()

if st.checkbox("Accéder au dataset"):
    num = st.number_input("Nombre de lignes souhaitées")
    st.dataframe(df.head(int(num)))
    
if st.button("Afficher noms des colonnes"):
    st.write(df.columns.tolist())
    st.write(df.dtypes)
    
occupation = st.multiselect("colonnes", df.columns.tolist())
st.write(df[occupation].dtypes)

if st.checkbox("Shape du dataset"):
    st.write(df.shape)
    
if st.checkbox("Statistiques descriptive"):
    st.write(df.describe())
    
if st.checkbox("Heatmap"):
    plt.figure(figsize=(2,2))
    ax = sns.heatmap(df.corr(), annot=True)
    #st._chart(ax)
    
if st.checkbox("histogramme"):
    serie = df['local_price']
    n = serie.count()
    n_bins = np.sqrt(n).astype(int)
    hist_values = np.histogram(
    serie, n_bins)
    st.bar_chart(hist_values)

if st.checkbox("Construisez votre graphique"):
    options = st.multiselect("colonnes à intégrer", df.columns.tolist())
    graphique = st.selectbox("graphique voulu",["histogramme","camembert","boîtes à moustache"])
    if graphique == "histogramme":
        serie = df[options]
        n=serie.count()
        n_bins=np.sqrt(n).astype(int)
        hist_values=np.histogram(serie,n_bins)
        st.bar_chart(hist_values)
    