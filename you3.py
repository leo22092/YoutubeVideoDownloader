import tkinter as tk
from pytube import YouTube
import utils

def download_video():
    link = entry_link.get()
    utils.download(link)
def download_audio():
    link=entry_link.get()
    utils.download_mp4(link)
def download_mp3():
    link=entry_link.get()
    utils.download_mp3(link)
def webm():
    link=entry_link.get()
    utils.download_webm(link)


def quality():
    pass
#     link = entry_link.get()
#     utils.qualities(link)
root = tk.Tk()
root.title("YouTube Downloader")
choices = ["Option 1", "Option 2", "Option 3", "Option 4"]
# selected_option = tk.StringVar()
# # selected_option.set(utils.qualities.choices[0])

# option_menu = tk.OptionMenu(root, selected_option, command=quality)
# option_menu.grid(row=8,column=2)



label1 = tk.Label(root, text="Paste Video Link:")
label1.grid(row=1,column=0)

entry_link = tk.Entry(root)
entry_link.grid(row=2,column=0)
link = entry_link.get()

submit_button = tk.Button(root, text="download video(HQ)", command=download_video)
submit_button.grid(row=4,column=2)

MP4_button = tk.Button(root, text="MP4", command=download_audio)
MP4_button.grid(row=4,column=3)

MP3_button = tk.Button(root, text="MP3", command=download_mp3)
MP3_button.grid(row=4,column=4)

webm_button = tk.Button(root, text="webm", command=download_audio)
webm_button.grid(row=5,column=2)

root.mainloop()
