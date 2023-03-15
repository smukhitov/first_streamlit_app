import streamlit as st
import pandas as pd
import requests

#reading file from AWS S3 bucket
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title("Healthy App!")
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = st.multiselect("Choose some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

st.header('Fruity Vice Fruit Advice')
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

#maiking API call get JSON and normalize it in df 
fruity_vice_response = requests.get('https://fruityvice.com/api/fruit/' + str(fruit_choice))
fruity_normalized = pd.json_normalize(fruity_vice_response.json())
st.dataframe(fruity_normalized)
