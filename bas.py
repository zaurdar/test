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
    p_temp_dir = tempfile.mkdtemp()
    st.image("CVM3D/fond/fond_test.jpg")
    if st.button("enter"):
        st.write(p_temp_dir+'/fond.jpg')
        temp_dir = p_temp_dir[1:]

        ndir= temp_dir + '/fond.jpg'
        st.write(ndir)
        shutil.copy("CVM3D/fond/fond_test.jpg", ndir)
        st.image(ndir)
app()