import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

st.title("Healthy App!")
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.multiselect("Choose some fruits: ", list(my_fruit_list.index))
st.dataframe(my_fruit_list)
