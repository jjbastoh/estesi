import streamlit as st
from PIL import Image

st.title("si")

st.header("en este espacio comienzo etc")
st.write("fácilmente etc")

image = Image.open("images.jpg")
st.image(image, caption="interfaces multi")
