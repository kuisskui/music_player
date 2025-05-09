import subprocess
from yt_dlp import YoutubeDL

import subprocess

class Media:
    def __init__(self, url):
        self.url = url


class Player:
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def play(self, media: Media):
        url = media.url
        ydl_opts = {'format': 'bestaudio/best', 'quiet': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        subprocess.run([
            'ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet',
            audio_url
        ])


class Playlist:
    def __init__(self, name, media_list):
        self.name = name
        self.media_list = media_list

    def add_media(self, media):
        self.media_list.append(media)
