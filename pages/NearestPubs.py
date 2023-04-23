import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static

st.header('Find the Nearest pub in your area.')

df = pd.read_csv("open_pubs_cleaned.csv")

x = df[['latitude', 'longitude']]

st.header('Find the Nearest pub in your area.')

lat = st.number_input('Enter latitude')
long = st.number_input('Enter longitude')
submit = st.button(label='submit')
y = np.array([lat, long])

dist = np.sqrt(np.sum((y - x) ** 2, axis=1))
k = 5
sort = np.argpartition(dist, k - 1)[:k]
if submit:
    m = folium.Map(location=[lat, long], zoom_start=13)
    tooltip = "Click to see pub details"
    for i in sort:
        pub = df.iloc[i]
        popup = f"{pub['name']}\n{pub['address']}"
        folium.Marker(
            location=[pub['latitude'], pub['longitude']],
            popup=popup,
            tooltip=tooltip
        ).add_to(m)

    folium_static(m)
