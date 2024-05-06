import subprocess
import streamlit as st
import tempfile
import os
import shutil
import sys
chemin_script = os.path.abspath(sys.argv[0])
path = os.path.dirname(chemin_script)
def extract():
    path_extract = os.path.join(path,"extract.bat")
    subprocess.run(path_extract,shell=True)
    path_mk = os.path.join(path, "mk.bat")
    subprocess.run(path_mk,shell=True)
def delete_cache():
    fichiers_a_supprimer = [
        os.path.join(path, "CVM3D\\vidéos\\projo_1.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_2.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_3.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_4.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_5.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_6.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_7.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_8.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_9.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_10.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_11.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_12.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_13.mp4"),
        os.path.join(path, "CVM3D\\vidéos\\projo_14.mp4"),
    ]

    # Suppression des fichiers
    for fichier in fichiers_a_supprimer:
        if os.path.exists(fichier):
            os.remove(fichier)
            print(f"Fichier {fichier} supprimé avec succès.")
        else:
            print(f"Le fichier {fichier} n'existe pas.")

st.title("App Projet 2024")
st.header('video creation')

st.write("chemin : "+str(path))



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

    n_file_path = os.path.join(path,"CVM3D/test.mp4")
    shutil.move(file_path, n_file_path)
if st.button("create edit"):
    extract()
if st.button("read video"):
    output_path = os.path.join(path,"CVM3D/output.mp4")
    st.video(output_path)
if st.button("empty the cache"):
    delete_cache()
st.header('video example')
st.subheader("l'attaque des titans :\n")
video_path = os.path.join(path,"CVM3D/exemple_snk.mp4")
st.video(video_path)