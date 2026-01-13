import streamlit as st

st.title("Make a simple calculator app")

num1 = st.number_input("Enter first number")

num2 = st.number_input("Enter second number")

operation = st.selectbox("choose the operation",['add','substract','multiply','divide'] )

result = 0
if st.button('calculate'):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'substract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 /num2

st.write("Result",result)