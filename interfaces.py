import streamlit as st
from PIL import Image

st.title("si")

st.header("en este espacio comienzo etc")
st.write("fácilmente etc")

image = Image.open("images.jpg")
st.image(image, caption="interfaces multi")

texto = st.text_input('el texto, es')
st.write('este coso?,texto')


st.subheader("ahora 2 col")
col1, col2 = st.columns(2)

with col1:
  st.subheader("esta es la col 1")
  st.write("las checkbox")
  resp = st.checkbox('estoy de acuerdo')
  if resp:
    st.write('correcto')

with col2:
  st.subheader("esta es la 2 col")
  modo = st.radio("que modalidad es la principal , ('visual' , 'audi' ,'lol'))if
  if modo == 'visual':
      st.write("la vista es fundamental para tu interfaz")

  if modo == "auditiva":
    st.write("la audicion es fundamental para tu interfaz")

  if modo == "tactil":
    st.write("el tactil es fundamenta para tu interfaz")
    
