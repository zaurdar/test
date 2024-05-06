import subprocess
import streamlit as st
import tempfile
import os
import shutil
import sys
chemin_script = os.path.abspath(sys.argv[0])
path = os.path.dirname(chemin_script)
def execute(string):
    list_cmd = string.split(",")
    for cmd in list_cmd:
        subprocess.run(cmd,shell=True)
activate = "streamlit run app.py"

x = 0
y = 0
delete_cmd ="del CVM3D/vidéos/projo_1.mp4," \
        "del CVM3D/videos/projo_2.mp4," \
        "del CVM3D/videos/projo_3.mp4," \
        "del CVM3D/videos/projo_4.mp4," \
        "del CVM3D/videos/projo_5.mp4," \
        "del CVM3D/videos/projo_6.mp4," \
        "del CVM3D/videos/projo_7.mp4," \
        "del CVM3D/videos/projo_8.mp4," \
        "del CVM3D/videos/projo_9.mp4," \
        "del CVM3D/videos/projo_10.mp4," \
        "del CVM3D/videos/projo_11.mp4," \
        "del CVM3D/videos/projo_12.mp4," \
        "del CVM3D/videos/projo_13.mp4," \
        "del CVM3D/videos/projo_14.mp4," \
        "del CVM3D/videos/temp_1.mp4," \
        "del CVM3D/videos/temp_2.mp4," \
        "del CVM3D/videos/temp_3.mp4," \
        "del CVM3D/videos/temp_4.mp4," \
        "del CVM3D/videos/temp_5.mp4," \
        "del CVM3D/videos/temp_6.mp4," \
        "del CVM3D/videos/temp_7.mp4," \
        "del CVM3D/videos/temp_8.mp4," \
        "del CVM3D/videos/temp_9.mp4," \
        "del CVM3D/videos/temp_10.mp4," \
        "del CVM3D/videos/temp_11.mp4," \
        "del CVM3D/videos/temp_12.mp4," \
        "del CVM3D/videos/temp_13.mp4," \
        "del CVM3D/videos/temp_14.mp4," \
        "del CVM3D/videos/output_1.mp4," \
        "del CVM3D/videos/output_2.mp4," \
        "del CVM3D/videos/output_3.mp4," \
        "del CVM3D/videos/output_4.mp4," \
        "del CVM3D/videos/output_5.mp4," \
        "del CVM3D/videos/output_6.mp4," \
        "del CVM3D/videos/output_7.mp4," \
        "del CVM3D/videos/output_8.mp4," \
        "del CVM3D/videos/output_9.mp4," \
        "del CVM3D/videos/output_10.mp4," \
        "del CVM3D/videos/output_11.mp4," \
        "del CVM3D/videos/output_12.mp4," \
        "del CVM3D/videos/output_13.mp4," \
        "del CVM3D/videos/output_14.mp4," \
        "del CVM3D/videos/output_15.mp4," \
        "del CVM3D/videos/audio.aac"

mk_cmd ='ffmpeg -i CVM3D/test.mp4 -vn -acodec copy CVM3D/videos/audio.aac -y,' \
    'ffmpeg -i houdain2.jpg -vf scale=1920:1080 houdain.jpg -y,' \
    'ffmpeg -i houdain.jpg -i CVM3D/videos/temp_1.mp4 -filter_complex "[0:v][1:v]overlay=722:435" CVM3D/videos/output_1.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_1.mp4 -i CVM3D/videos/temp_2.mp4 -filter_complex "[0:v][1:v]overlay=722:514" CVM3D/videos/output_2.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_2.mp4 -i CVM3D/videos/temp_3.mp4 -filter_complex "[0:v][1:v]overlay=788:435" CVM3D/videos/output_3.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_3.mp4 -i CVM3D/videos/temp_4.mp4 -filter_complex "[0:v][1:v]overlay=788:514" CVM3D/videos/output_4.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_4.mp4 -i CVM3D/videos/temp_5.mp4 -filter_complex "[0:v][1:v]overlay=853:435" CVM3D/videos/output_5.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_5.mp4 -i CVM3D/videos/temp_6.mp4 -filter_complex "[0:v][1:v]overlay=853:514" CVM3D/videos/output_6.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_6.mp4 -i CVM3D/videos/temp_7.mp4 -filter_complex "[0:v][1:v]overlay=928:435" CVM3D/videos/output_7.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_7.mp4 -i CVM3D/videos/temp_8.mp4 -filter_complex "[0:v][1:v]overlay=928:514" CVM3D/videos/output_8.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_8.mp4 -i CVM3D/videos/temp_9.mp4 -filter_complex "[0:v][1:v]overlay=1001:435" CVM3D/videos/output_9.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_9.mp4 -i CVM3D/videos/temp_10.mp4 -filter_complex "[0:v][1:v]overlay=1001:514" CVM3D/videos/output_10.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_10.mp4 -i CVM3D/videos/temp_11.mp4 -filter_complex "[0:v][1:v]overlay=1067:435" CVM3D/videos/output_11.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_11.mp4 -i CVM3D/videos/temp_12.mp4 -filter_complex "[0:v][1:v]overlay=1067:514" CVM3D/videos/output_12.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_12.mp4 -i CVM3D/videos/temp_13.mp4 -filter_complex "[0:v][1:v]overlay=1133:435" CVM3D/videos/output_13.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_13.mp4 -i CVM3D/videos/temp_14.mp4 -filter_complex "[0:v][1:v]overlay=1133:514" CVM3D/videos/output_14.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_14.mp4 -vf "eq=brightness=-0.15:contrast=0.5:saturation=1.5" -c:a copy CVM3D/videos/output_15.mp4 -y,' \
    'ffmpeg -i CVM3D/videos/output_15.mp4 -i CVM3D/videos/audio.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest CVM3D/output.mp4 -y'
file_path=""

st.title("App Projet 2024")


st.write("chemin : "+str(path))

st.header('video example')
st.subheader("l'attaque des titans :\n")
video_path = os.path.join(path,"CVM3D/exemple_snk.mp4")
st.video(video_path)

st.header("calibrage")
x = st.slider("coordonnée x ",0,1920)
y = st.slider("coordonnée y ",0,1080)
if st.button("enter"):
    test_fond_cmd = 'ffmpeg -i CVM3D/fond/fond_test.jpg -vf scale=1920:1080 CVM3D/fond/fond.jpg -y,' \
                    'ffmpeg -i CVM3D/fond/fond.jpg -vf "drawbox=x=' + str(x) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 160) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 160) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 2 * (160)) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 2 * (160)) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 3 * (160)) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 3 * (160)) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 4 * (160)) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 4 * (160)) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 5 * (160)) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 5 * (160)) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,' \
                   'ffmpeg -i CVM3D/fond/fond_2.jpg -vf "drawbox=x=' + str(x + 6 * (160)) + ':y=' + str(
        y) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_1.jpg -y,' \
             'ffmpeg -i CVM3D/fond/fond_1.jpg -vf "drawbox=x=' + str(x + 6 * (160)) + ':y=' + str(
        y + 330) + ':w=120:h=210:color=green@0.5" CVM3D/fond/fond_2.jpg -y,'

    execute(test_fond_cmd)
    st.image("CVM3D/fond/fond_2.jpg")
st.header('video creation')
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
    extract_cmd = 'ffmpeg -i '+file_path+' -vf scale=1920:1080 output.mp4 -y,' \
                  'mkdir "CVM3D/videos",' \
                  'ffmpeg -i output.mp4 -vf crop=120:210:' + str(x) + ':' + str(y) + ' CVM3D/videos/projo_1.mp4 -y,' \
                                                                                     'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(
        x) + ':' + str(y + 330) + ' CVM3D/videos/projo_2.mp4 -y,' \
                                  'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 160) + ':' + str(
        y) + ' CVM3D/videos/projo_3.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 160) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_4.mp4 -y,' \
                   'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 2 * (160)) + ':' + str(
        y) + ' CVM3D/videos/projo_5.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 2 * (160)) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_6.mp4 -y,' \
                   'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 3 * (160)) + ':' + str(
        y) + ' CVM3D/videos/projo_7.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 3 * (160)) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_8.mp4 -y,' \
                   'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 4 * (160)) + ':' + str(
        y) + ' CVM3D/videos/projo_9.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 4 * (160)) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_10.mp4 -y,' \
                   'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 5 * (160)) + ':' + str(
        y) + ' CVM3D/videos/projo_11.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 5 * (160)) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_12.mp4 -y,' \
                   'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 6 * (160)) + ':' + str(
        y) + ' CVM3D/videos/projo_13.mp4 -y,' \
             'ffmpeg -i CVM3D/test.mp4 -vf crop=120:210:' + str(x + 6 * (160)) + ':' + str(
        y + 330) + ' CVM3D/videos/projo_14.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_1.mp4 -vf scale=36:50 CVM3D/videos/temp_1.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_2.mp4 -vf scale=36:50 CVM3D/videos/temp_2.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_3.mp4 -vf scale=36:50 CVM3D/videos/temp_3.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_4.mp4 -vf scale=36:50 CVM3D/videos/temp_4.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_5.mp4 -vf scale=36:50 CVM3D/videos/temp_5.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_6.mp4 -vf scale=36:50 CVM3D/videos/temp_6.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_7.mp4 -vf scale=36:50 CVM3D/videos/temp_7.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_8.mp4 -vf scale=36:50 CVM3D/videos/temp_8.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_9.mp4 -vf scale=36:50 CVM3D/videos/temp_9.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_10.mp4 -vf scale=36:50 CVM3D/videos/temp_10.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_11.mp4 -vf scale=36:50 CVM3D/videos/temp_11.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_12.mp4 -vf scale=36:50 CVM3D/videos/temp_12.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_13.mp4 -vf scale=36:50 CVM3D/videos/temp_13.mp4 -y,' \
                   'ffmpeg -i CVM3D/videos/projo_14.mp4 -vf scale=36:50 CVM3D/videos/temp_14.mp4 -y'
    execute(extract_cmd)
    st.write("ok")
    execute(mk_cmd)
if st.button("read video"):
    output_path = os.path.join(path,"CVM3D/output.mp4")
    st.video(output_path)
if st.button("empty the cache"):
    execute(delete_cmd)
st.header("downloads")
col1,col2 = st.columns(2)
with col1:
    shutil.make_archive("files", 'zip', "CVM3D/videos")
    doss = open("files.zip", "rb").read()
    st.download_button("download files",doss,"photos.zip")
with col2:
    im = open("CVM3D/output.mp4", "rb").read()
    st.download_button("download video",im,"video.mp4")

