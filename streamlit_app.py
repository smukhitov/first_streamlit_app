import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

st.title("Hello from my App!")
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
st.dataframe(my_fruit_list)
