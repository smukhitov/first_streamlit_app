import streamlit as st
import pandas as pd
import requests
import snowflake.connector


#reading file from AWS S3 bucket
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title("Healthy App!")
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = st.multiselect("Choose some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

st.header('Fruity Vice Fruit Advice')

# Creates a text input box where fruit name is entered
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

#maiking API call get JSON and normalize it in df 
fruity_vice_response = requests.get('https://fruityvice.com/api/fruit/' + str(fruit_choice))
fruity_normalized = pd.json_normalize(fruity_vice_response.json())
st.dataframe(fruity_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.all()
st.text("The fruit load list contains:")
st.text(my_data_rows)
