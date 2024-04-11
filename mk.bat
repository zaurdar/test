cd C:\Users\gabriel\Desktop\test_webapp
IF EXIST "CVM3D\vidéos\projo_1.mp4" (
    ffmpeg -i CVM3D\test.mp4 -vn -acodec copy CVM3D\vidéos\audio.aac
    ffmpeg -i houdain2.jpg -vf scale=1920:1080 houdain.jpg
    ffmpeg -i houdain.jpg -i CVM3D\vidéos\temp_1.mp4 -filter_complex "[0:v][1:v]overlay=722:435" CVM3D\vidéos\output_1.mp4
    ffmpeg -i CVM3D\vidéos\output_1.mp4 -i CVM3D\vidéos\temp_2.mp4 -filter_complex "[0:v][1:v]overlay=722:514" CVM3D\vidéos\output_2.mp4
    ffmpeg -i CVM3D\vidéos\output_2.mp4 -i CVM3D\vidéos\temp_3.mp4 -filter_complex "[0:v][1:v]overlay=788:435" CVM3D\vidéos\output_3.mp4
    ffmpeg -i CVM3D\vidéos\output_3.mp4 -i CVM3D\vidéos\temp_4.mp4 -filter_complex "[0:v][1:v]overlay=788:514" CVM3D\vidéos\output_4.mp4
    ffmpeg -i CVM3D\vidéos\output_4.mp4 -i CVM3D\vidéos\temp_5.mp4 -filter_complex "[0:v][1:v]overlay=853:435" CVM3D\vidéos\output_5.mp4
    ffmpeg -i CVM3D\vidéos\output_5.mp4 -i CVM3D\vidéos\temp_6.mp4 -filter_complex "[0:v][1:v]overlay=853:514" CVM3D\vidéos\output_6.mp4
    ffmpeg -i CVM3D\vidéos\output_6.mp4 -i CVM3D\vidéos\temp_7.mp4 -filter_complex "[0:v][1:v]overlay=928:435" CVM3D\vidéos\output_7.mp4
    ffmpeg -i CVM3D\vidéos\output_7.mp4 -i CVM3D\vidéos\temp_8.mp4 -filter_complex "[0:v][1:v]overlay=928:514" CVM3D\vidéos\output_8.mp4
    ffmpeg -i CVM3D\vidéos\output_8.mp4 -i CVM3D\vidéos\temp_9.mp4 -filter_complex "[0:v][1:v]overlay=1001:435" CVM3D\vidéos\output_9.mp4
    ffmpeg -i CVM3D\vidéos\output_9.mp4 -i CVM3D\vidéos\temp_10.mp4 -filter_complex "[0:v][1:v]overlay=1001:514" CVM3D\vidéos\output_10.mp4
    ffmpeg -i CVM3D\vidéos\output_10.mp4 -i CVM3D\vidéos\temp_11.mp4 -filter_complex "[0:v][1:v]overlay=1067:435" CVM3D\vidéos\output_11.mp4
    ffmpeg -i CVM3D\vidéos\output_11.mp4 -i CVM3D\vidéos\temp_12.mp4 -filter_complex "[0:v][1:v]overlay=1067:514" CVM3D\vidéos\output_12.mp4
    ffmpeg -i CVM3D\vidéos\output_12.mp4 -i CVM3D\vidéos\temp_13.mp4 -filter_complex "[0:v][1:v]overlay=1133:435" CVM3D\vidéos\output_13.mp4
    ffmpeg -i CVM3D\vidéos\output_13.mp4 -i CVM3D\vidéos\temp_14.mp4 -filter_complex "[0:v][1:v]overlay=1133:514" CVM3D\vidéos\output_14.mp4
    ffmpeg -i CVM3D\vidéos\output_14.mp4 -vf "eq=brightness=-0.15:contrast=0.5:saturation=1.5" -c:a copy CVM3D\vidéos\output_15.mp4
    ffmpeg -i CVM3D\vidéos\output_15.mp4 -i CVM3D\vidéos\audio.aac -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest CVM3D\output.mp4

) ELSE (
    echo Le fichier n'existe pas.
)

