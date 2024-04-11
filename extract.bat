cd C:\Users\gabriel\Desktop\test_webapp
IF EXIST "CVM3D\test.mp4" (

    ffmpeg -i CVM3D\test.mp4 -vf scale=1920:1080 output.mp4
    mkdir "CVM3D\vidéos"
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:0:165 CVM3D\vidéos\projo_1.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:0:495 CVM3D\vidéos\projo_2.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:160:165 CVM3D\vidéos\projo_3.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:160:495 CVM3D\vidéos\projo_4.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:320:165 CVM3D\vidéos\projo_5.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:320:495 CVM3D\vidéos\projo_6.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:480:165 CVM3D\vidéos\projo_7.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:480:495 CVM3D\vidéos\projo_8.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:640:165 CVM3D\vidéos\projo_9.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:640:495 CVM3D\vidéos\projo_10.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:800:165 CVM3D\vidéos\projo_11.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:800:495 CVM3D\vidéos\projo_12.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:960:165 CVM3D\vidéos\projo_13.mp4
    ffmpeg -i CVM3D\test.mp4 -vf crop=120:210:960:495 CVM3D\vidéos\projo_14.mp4
    ffmpeg -i CVM3D\vidéos\projo_1.mp4 -vf scale=36:50 CVM3D\vidéos\temp_1.mp4
    ffmpeg -i CVM3D\vidéos\projo_2.mp4 -vf scale=36:50 CVM3D\vidéos\temp_2.mp4
    ffmpeg -i CVM3D\vidéos\projo_3.mp4 -vf scale=36:50 CVM3D\vidéos\temp_3.mp4
    ffmpeg -i CVM3D\vidéos\projo_4.mp4 -vf scale=36:50 CVM3D\vidéos\temp_4.mp4
    ffmpeg -i CVM3D\vidéos\projo_5.mp4 -vf scale=36:50 CVM3D\vidéos\temp_5.mp4
    ffmpeg -i CVM3D\vidéos\projo_6.mp4 -vf scale=36:50 CVM3D\vidéos\temp_6.mp4
    ffmpeg -i CVM3D\vidéos\projo_7.mp4 -vf scale=36:50 CVM3D\vidéos\temp_7.mp4
    ffmpeg -i CVM3D\vidéos\projo_8.mp4 -vf scale=36:50 CVM3D\vidéos\temp_8.mp4
    ffmpeg -i CVM3D\vidéos\projo_9.mp4 -vf scale=36:50 CVM3D\vidéos\temp_9.mp4
    ffmpeg -i CVM3D\vidéos\projo_10.mp4 -vf scale=36:50 CVM3D\vidéos\temp_10.mp4
    ffmpeg -i CVM3D\vidéos\projo_11.mp4 -vf scale=36:50 CVM3D\vidéos\temp_11.mp4
    ffmpeg -i CVM3D\vidéos\projo_12.mp4 -vf scale=36:50 CVM3D\vidéos\temp_12.mp4
    ffmpeg -i CVM3D\vidéos\projo_13.mp4 -vf scale=36:50 CVM3D\vidéos\temp_13.mp4
    ffmpeg -i CVM3D\vidéos\projo_14.mp4 -vf scale=36:50 CVM3D\vidéos\temp_14.mp4
) ELSE (
    echo Le fichier n'existe pas.
)