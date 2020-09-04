from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def download_and_crop(url, start_time, end_time, path):
    ffmpeg_extract_subclip(YouTube(url).streams.get_highest_resolution().download('tmp/', "temp_vid"), start_time, end_time, targetname=path)
