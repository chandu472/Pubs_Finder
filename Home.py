import streamlit as st
import pandas as pd




df = pd.read_csv("open_pubs_cleaned.csv")

st.title("Welcome to the Pub Finder App!")
st.write("With this app, you can find pubs in the United Kingdom based on location and proximity to your current location.")
st.write("To get started, use the navigation menu on the left to choose an option.")
 
st.header("Pub Data Statistics")
st.write(f"Total number of pubs in the dataset: {len(df)}")
st.write(f"Number of unique postal codes: {len(df['postcode'].unique())}")
st.write(f"Number of unique local authorities: {len(df['local_authority'].unique())}")
st.write(f"Average latitude of pubs: {df['latitude'].mean()}")
st.write(f"Average longitude of pubs: {df['longitude'].mean()}")
st.write(df.describe())
