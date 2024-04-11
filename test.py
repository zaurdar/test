import cv2
import streamlit as st
import numpy as np
import tempfile
from IPython.display import display
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import moviepy.editor as mpe
file_path = ""


def cropandscotch(im1, im2, x1, x2, y1, y2):
    a = np.shape(im1)
    b = np.shape(im2)

    d0 = round(a[0] / b[0], 2)
    d1 = round(a[1] / b[1], 2)
    im2 = list(im2)
    im1 = list(im1)
    im3 = []
    # zone image 1 uniquement
    for i in range(0, y1):
        im3.append(im1[i])

    # zone image 2 et image 1
    for i in range(y1, y2):
        it = []
        for j in range(0, x1):
            it.append(im1[i][j])
        for k in range(x1, x2):
            it.append(im2[round(i / d0)][round(k / d1)])
        for l in range(x2, a[1]):
            it.append(im1[i][l])
        im3.append(it)
    # zone image 1 uniquement
    for i in range(y2, a[0]):
        im3.append(im1[i])
    im3 = np.array(im3)
    return im3


# In[52]:


def create_simulation():
    cap = cv2.VideoCapture(file_path)

    im1 = cv2.imread("C:/Users/gabriel/Desktop/test_webapp/houdain2.jpg", 1)

    a = np.shape(im1)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videowriter = cv2.VideoWriter("vidéo_test.mp4", fourcc, 30, (a[1], a[0]));
    while True:
        tab = []
        ret, frame = cap.read()
        # fenetres gauches
        im3 = cropandscotch(im1, frame, 385, 405, 275, 310)
        im3 = cropandscotch(im3, frame, 385, 405, 325, 360)
        im3 = cropandscotch(im3, frame, 420, 440, 275, 310)
        im3 = cropandscotch(im3, frame, 420, 440, 325, 360)
        im3 = cropandscotch(im3, frame, 455, 475, 275, 310)
        im3 = cropandscotch(im3, frame, 455, 475, 325, 360)
        e = 184
        # fenetres droites
        im3 = cropandscotch(im3, frame, 350 + e, 370 + e, 275, 310)
        im3 = cropandscotch(im3, frame, 350 + e, 370 + e, 325, 360)
        im3 = cropandscotch(im3, frame, 385 + e, 405 + e, 275, 310)
        im3 = cropandscotch(im3, frame, 385 + e, 405 + e, 325, 360)
        im3 = cropandscotch(im3, frame, 420 + e, 440 + e, 275, 310)
        im3 = cropandscotch(im3, frame, 420 + e, 440 + e, 325, 360)
        # fenetres milieu
        im3 = cropandscotch(im3, frame, 493, 517, 275, 310)
        im3 = cropandscotch(im3, frame, 493, 517, 325, 360)
        videowriter.write(im3)
        cv2.imshow('houdain', im3)

        if cv2.waitKey(1) == 27:
            break
    cap.release()
    videowriter.release()
    cv2.destroyAllWindows()


# In[53]:






def extract_audio(video_file_path, audio_file_path):
    video_clip = mpe.VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file_path, codec='mp3')


# In[56]:


def play_video(video_file_path, audio_file_path):
    video = VideoFileClip(video_file_path)
    audio = AudioFileClip(audio_file_path)

    # Fusionner la vidéo avec le nouveau son
    video_with_audio = video.set_audio(audio)
    display(video_with_audio.ipython_display(loop=True, autoplay=True, maxduration=300))

def play():
    video_file = file_path
    audio_file = "audio.mp3"
    extract_audio(video_file, audio_file)
    video_file = "vidéo_test.mp4"
    play_video(video_file, audio_file)


# In[60]:










st.title("App Projet 2024")
st.header('video creation')
mdp = st.text_input("entrez le mdp")
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
if st.button("create edit"):
    if mdp =="123":
        create_simulation()
        play()
if st.button("read video"):
    st.video("__temp__.mp4")

st.header('video example')
st.subheader('skyfall :\n')
st.video("C:/Users/gabriel/Desktop/test_webapp/__temp__ skyfall.mp4")