import streamlit as st

#streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square ,cube , and fifth power")

#get user input
n=st.number_input("Enter an integer",value=1,step=1)

#calculate result
square=n**2
cube=n**3
fifth_power=n**5

#display the result
st.write(f"square of {n} is:{square}")
st.write(f"cube of {n} is:{cube}")
st.write(f"fifth power of {n} is:{fifth_power}")