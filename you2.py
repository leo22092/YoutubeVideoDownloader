from pytube import YouTube

# get the YouTube video link from user
link = input("https://youtu.be/mEXAm9lTIBM")

# create YouTube object and get all available streams
try:
    yt = YouTube(link)
    print(f"Available streams for video: {yt.title}")
    streams = yt.streams.all()
    for stream in streams:
        print(stream)
except Exception as e:
    print("Error getting available streams:", e)