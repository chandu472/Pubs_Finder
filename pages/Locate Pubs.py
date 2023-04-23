import streamlit as st
import pandas as pd

df = pd.read_csv("open_pubs_cleaned.csv")

st.title('Search for Pubs by Postcode or Local Authority')


option = st.selectbox('Select a search option:', ['Postcode', 'Local Authority'])

if option == 'Postcode':
   
    form = st.form(key='my_form')
    postcode = form.selectbox('Select a postcode:', df['postcode'].unique())
    submit = form.form_submit_button(label='Submit')
    
   
    lat = df.loc[df['postcode'] == postcode, 'latitude']
    long = df.loc[df['postcode'] == postcode, 'longitude']
    rdf = pd.DataFrame((lat, long)).T
    st.map(rdf)

elif option == 'Local Authority':
    
    form = st.form(key='my_form')
    local_auth = form.selectbox('Select a local authority:', df['local_authority'].unique())
    submit = form.form_submit_button(label='Submit')
    
    
    lat = df.loc[df['local_authority'] == local_auth, 'latitude']
    long = df.loc[df['local_authority'] == local_auth, 'longitude']
    rdf = pd.DataFrame((lat, long)).T
    st.map(rdf)
