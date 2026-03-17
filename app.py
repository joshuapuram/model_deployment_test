import streamlit as st

# Set the app title
st.title('My First Streamlit App')

# Add a welcome message
st.write('Welcome to my Streamlit app! This is a simple example.')

# Add an interactive widget (a slider)
x = st.slider("Select a value")

# Display the value and its square
st.write(x, "squared is", x * x)
