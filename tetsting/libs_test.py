import moviepy.editor
name_video = input("write name video: ")
name_audio = input("write name audio: ")
video = moviepy.editor.VideoFileClip(name_video)
audio = video.audio
audio.write_audiofile(name_audio)
input("press any key........")