import subprocess
from yt_dlp import YoutubeDL
from model.media import Media


class Player:
    _instances = {}

    def __init__(self):
        self.current_url = ""

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

    def set_current_url(self, url):
        self.current_url = url


player = Player()
