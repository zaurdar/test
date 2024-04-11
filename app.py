import subprocess
import streamlit as st
import tempfile
import os
import shutil
import sys
def extract():
    subprocess.run("extract.bat")
    subprocess.run("mk.bat")
def delete_cache():
    subprocess.run("delete.bat")

st.title("App Projet 2024")
st.header('video creation')
chemin_script = os.path.abspath(sys.argv[0])
st.write(chemin_script)

file = st.file_uploader("entrez la video à editer")
if file is not None:
    # Créer un fichier temporaire
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    # Écrire les données binaires du fichier dans le fichier temporaire
    temp_file.write(file.read())

    # Fermer le fichier temporaire
    temp_file.close()

    # Obtenez le chemin du fichier temporaire
    file_path = temp_file.name

    # Afficher le chemin du fichier temporaire
    st.write("Le fichier est enregistré temporairement à :", file_path)
    nom_fichier, extension = os.path.splitext(file_path)

    n_file_path = "CVM3D/test.mp4"
    shutil.move(file_path, n_file_path)
if st.button("create edit"):
    extract()
if st.button("read video"):
    st.video("CVM3D/output.mp4")
if st.button("empty the cache"):
    delete_cache()
st.header('video example')
st.subheader("l'attaque des titans :\n")
st.video("CVM3D/exemple_snk.mp4")