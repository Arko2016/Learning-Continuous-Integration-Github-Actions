import streamlit as st

#APP headers
st.title("Simple Calculator App")
st.write("Find the square, cube and fifth power of a given number")

#Take input
num = st.number_input("Enter number:", value = 1, step = 1)

#Perform calculations
sq = round(num ** 2,0)
cu = round(num ** 3,0)
fp = round(num ** 5,0)

#Display results
st.write(f"Square of {num}: {sq}")
st.write(f"Cube of {num}: {cu}")
st.write(f"Fifth Power of {num}: {fp}")
