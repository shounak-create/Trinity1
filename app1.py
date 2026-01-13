import streamlit as st

st.title("Some basic command in streamlit.")
name = st.text_input("Enter your name: ")

if st.button('submit'):
    st.write("hello" , name)

age = st.slider("Select you age",1,100)
city = st.selectbox("select your city",['pune','mumbai','delhi','bangalore'])
if st.button("Show details"):
    st.write("age", age)
    st.write("city", city)