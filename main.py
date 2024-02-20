import PySimpleGUI as sg
from pytube import YouTube as yt
import os

homeDir = os.path.expanduser("~")
PATH = homeDir + r"\YT-Downloader"

def get_video(url):
    try:
        yt_video = yt(url)
        return yt_video
    except:
        return False


# Elements in window.
layout = [[sg.Text('URL:'), sg.InputText()], [sg.Text('', key="video_name")],
          [sg.Button('Download MP3'), sg.Button('Download MP4'), sg.Button("Open Path")]]

# Create the Window
window = sg.Window('YT-Video Downloader', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    elif event == "Download MP3":
        yt_video = get_video(values[0])
        if yt_video:
            window["video_name"].update("Download MP3: " + yt_video.title)
            audio = yt_video.streams.filter(only_audio=True).first()
            audio.download(filename=f"{audio.title}.mp3", output_path=PATH + "/MP3")
        else:
            window["video_name"].update("Error: Video not found")
    elif event == "Download MP4":
        yt_video = get_video(values[0])
        if yt_video:
            window["video_name"].update("Download MP4: " + yt_video.title)
            video = yt_video.streams.get_highest_resolution()
            video.download(PATH + "/MP4")
        else:
            window["video_name"].update("Error: Video not found")
    elif event == "Open Path":
        os.startfile(PATH)

window.close()
