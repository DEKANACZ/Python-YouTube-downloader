import youtube_dl
from yt_dlp import YoutubeDL
import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

(option,C1,C2,C3) = [dict(format="bestaudio/best" ,extracaudio=True), "https://youtu.be", "https://www.youtube.com", "https://youtube.com"]
def download(link) :
    if  not (C1 in link or C2 in link or C3 in link):
        quit("[!] Invalid video URL\n")
    with YoutubeDL(option) as YTA:
        YTA.download([link])
    return True
if __name__ == "__main__":
    url = input("Enter your URL video: ")
    if download(url):
        print("\n[+] Audio Downloaded... \n")


