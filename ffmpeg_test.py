import ffmpeg
video = ffmpeg.input('audio.mp3')
video.output('output.mp3').run()

