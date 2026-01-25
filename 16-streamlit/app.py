import streamlit as st
import pandas as pd
import numpy as np
## Command to run = streamlit run app.py
## Title of the aplication
st.title("Hello Streamlit")

## Diplay a Simple Text
st.write("This is a imple text")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


## Display the Dataframe
st.write("Here is the dataframe")
st.write(df)


##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)

name = st.text_input("Enter name")
age=st.slider("Select you age",0,100,25)
option=['a','b','c']
choice=st.selectbox("Choose Lang",option)

st.write(f"Your Name is {name} and age is {age} and choice is {choice}")
uploaded_file=st.file_uploader("Choose a file",type="csv")
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)