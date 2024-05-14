import streamlit as st
st.slider("echelle de confiance")
txt = st.text_input("entrez ")
if st.button("mettre un message"):

    st.write(txt)
st.image("coeur.png")