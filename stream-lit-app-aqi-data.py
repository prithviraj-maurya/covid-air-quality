import streamlit as st
import pandas as pd
import numpy as np

st.title('Air Quality EDA')

## Read data
data_path = './data/city_day.csv'
cities_coord_path = './data/indian_cities_coord.csv'

def load_data():
    data = pd.read_csv(data_path)
    cities_coord = pd.read_csv(cities_coord_path)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    cities_coord.rename(lowercase, axis='columns', inplace=True)
    data['date'] = pd.to_datetime((data['date']))
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    # combine the coordinates of the cities
    data = data.merge(cities_coord, on="city", how='inner')
    return data

# Load 1k rows
data = load_data()
# Notify the user
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data.head())

## Map all the cities present in the dataset
year = st.slider('Year', 2015, 2020, 2020)
filtered_data = data[data['date'].dt.year == year]
st.subheader(f'Map of all cities in the year {year}')
st.map(filtered_data)
