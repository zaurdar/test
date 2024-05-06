import subprocess
import streamlit as st
import tempfile
import os
import shutil
import sys

def app():
    chemin_script = os.path.abspath(sys.argv[0])
    path = os.path.dirname(chemin_script)

    def execute(string):
        list_cmd = string.split(",")
        for cmd in list_cmd:
            subprocess.run(cmd, shell=True)


    x = 0
    y = 0

    st.title("App Projet 2024")

    st.write("chemin : " + str(path))

    st.header('video example')
    st.subheader("l'attaque des titans :\n")
    video_path = os.path.join(path, "CVM3D/exemple_snk.mp4")
    st.video(video_path)

    st.header("calibrage")
    x = st.slider("coordonnée x ", 0, 1920)
    y = st.slider("coordonnée y ", 0, 1080)
    temp_dir = tempfile.mkdtemp()
    st.image("CVM3D/fond/fond_test.jpg")
    if st.button("enter"):

        # Copier l'image dans le dossier temporaire
        shutil.copy("CVM3D/fond/fond_test.jpg", temp_dir)

        # Obtenir le nom de l'image dans le dossier temporaire
        image_filename = os.path.basename("CVM3D/fond/fond_test.jpg")
        st.write(image_filename)
        # Chemin vers l'image dans le dossier temporaire
        image_temp_path = os.path.join(temp_dir, image_filename)
        st.write(image_temp_path)
        st.image("image_temp_path")
app()