import streamlit as st
from PIL import Image

st.title("si")

st.header("en este espacio comienzo etc")
st.write("fácilmente etc")

image = Image.open("images.jpg")
st.image(image, caption="interfaces multi")

texto = st.text_input("el texto, es")
st.write("este coso?, texto")


st.subheader("ahora 2 col")
col1, col2 = st.columns(2)

with col1:
    st.subheader("esta es la col 1")
    st.write("las checkbox")

    resp = st.checkbox("estoy de acuerdo")

    if resp:
        st.write("correcto")


with col2:
    st.subheader("esta es la 2 col")

    modo = st.radio(
        "¿Qué modalidad es la principal?",
        ("visual", "auditiva", "táctil")
    )

    if modo == "visual":
        st.write("La vista es fundamental para tu interfaz")

    if modo == "auditiva":
        st.write("La audición es fundamental para tu interfaz")

    if modo == "táctil":
        st.write("El táctil es fundamental para tu interfaz")
