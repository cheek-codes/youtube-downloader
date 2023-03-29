from pytube import YouTube
import os

yt = YouTube(input("url link: "))

video = yt.streams.filter(only_audio = True).first()

destination = "C:/Users/sandy/downloads"

out = video.download(output_path=destination)

base, ext = os.path.splitext(out)
new = base + ".mp3"
os.rename(out, new)

print(f"{yt.title} has been downloaded")