import streamlit as st
from PIL import Image
st.title("si")

st.header("en este espacio comienxo etc")
st.write("facilmente etc")
image = Image.open('images.png')
st.image(image, caption ='interfaces multi')
