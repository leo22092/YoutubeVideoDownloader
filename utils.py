
from pytube import YouTube
from pydub import AudioSegment
import os

def download(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading video: {yt.title}")
        stream.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error downloading video:", e)

def qualities(link):
    choices=[]
    try:
        yt = YouTube(link)
        print(f"Available streams for video: {yt.title}")
        streams = yt.streams.all()
        for stream in streams:
            print(stream)
            choices.append(stream.mime_type)
        return choices
    except Exception as e:
        print("Error getting available streams:", e)
        choices = ["Option 1", "Option 2", "Option 3", "Option 4"]





def download_mp4(link, output_path=None):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading audio: {yt.title}")
        if output_path:
            stream.download(output_path=output_path, filename_prefix=yt.title)
        else:
            stream.download(filename_prefix=yt.title)
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error downloading audio:", e)


def download_webm(link, output_path=None):
    try:
        yt = YouTube(link)
        stream = yt.streams.filter(file_extension='webm').order_by('resolution').desc().first()
        print(f"Downloading video: {yt.title}")
        if output_path:
            stream.download(output_path=output_path, filename_prefix=yt.title)
        else:
            stream.download(filename_prefix=yt.title)
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error downloading video:", e)



def download_mp3_old(link, output_path=None):
    try:
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        print(f"Downloading audio: {yt.title}")
        if output_path:
            audio_file_path = audio_stream.download(output_path=output_path, filename_prefix=yt.title)
        else:
            audio_file_path = audio_stream.download(filename_prefix=yt.title)
        audio_file = AudioSegment.from_file(audio_file_path, format='mp4')
        mp3_file_path = audio_file_path[:-4] + ".mp3"
        audio_file.export(mp3_file_path, format='mp3')
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error downloading audio:", e)

from pytube import YouTube

def download_webm_new(link, output_path=None):
    try:
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        print(f"Downloading audio: {yt.title}")
        if output_path:
            audio_file_path = audio_stream.download(output_path=output_path, filename_prefix=yt.title, skip_existing=False)
        else:
            audio_file_path = audio_stream.download(filename_prefix=yt.title, skip_existing=False)
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error downloading audio:", e)

# Example usage
# download_mp3('https://www.youtube.com/watch?v=VIDEO_ID', output_path='output')
def download_mp3_without_sanitize(link, output_path=None):
    try:
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        print(f"Downloading high-quality MP3: {yt.title}")

        if output_path:
            os.makedirs(output_path, exist_ok=True)
            mp3_file_path = os.path.join(output_path, f"{yt.title}.mp3")
        else:
            mp3_file_path = f"{yt.title}.mp3"

        audio_stream.download(output_path=output_path, filename=yt.title)
        os.rename(os.path.join(output_path, f"{yt.title}.{audio_stream.subtype}"), mp3_file_path)

        print("High-quality MP3 downloaded successfully!")
    except Exception as e:
        print("Error downloading high-quality MP3:", e)






import re

# Function to sanitize the video title
def sanitize_title(title):
    # Remove special characters and replace them with underscores
    sanitized_title = re.sub(r'[^\w\s-]', '', title)
    sanitized_title = re.sub(r'[-\s]+', '-', sanitized_title)
    return sanitized_title
    print(sanitize_title)
# Function to download high-quality MP3 audio
def download_mp3(url):
    video_id = get_video_id(url)
    if video_id:
        try:
            # Retrieve video details using YouTube Data API
            video_details = youtube.videos().list(part='snippet', id=video_id).execute()
            video_title = video_details['items'][0]['snippet']['title']
            
            # Sanitize the video title
            sanitized_title = sanitize_title(video_title)
            
            # Configure youtube_dl options for MP3 extraction
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'outtmpl': f'{sanitized_title}.%(ext)s',
            }
            
            # Download the MP3 audio using youtube_dl
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            print("High-quality MP3 downloaded successfully!")
        except Exception as e:
            print("Error downloading high-quality MP3:", e)
    else:
        print("Invalid YouTube video URL")
