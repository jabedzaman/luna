import os
from pytube import YouTube

# Prompt the user for the YouTube video URL
def ytdl():
    url = input("Enter the YouTube video URL: ")
    download_dir = input("Enter the download directory: ")

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        filename = video.default_filename
        video.download(download_dir)
        print(f"Video downloaded to {download_dir}/{filename}")
    except Exception as e:
        print(f"An error occurred: {e}")
