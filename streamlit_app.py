import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfat Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spniach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



#  Importing pandas and reading a CSV file
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
