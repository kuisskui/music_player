import subprocess
from yt_dlp import YoutubeDL
from model.media import Media
from model.player_status import PlayerStatus


class Player:
    _instances = {}

    def __init__(self):
        self._proc = None
        self.__proc = None
        self.current_url = ""
        self.__status: PlayerStatus = PlayerStatus.READY

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def play(self, media: Media):
        self.__status = PlayerStatus.LOADING
        url = media.url
        ydl_opts = {'format': 'bestaudio/best', 'quiet': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        cmd = [
            'ffplay',
            '-nodisp', '-autoexit', '-loglevel', 'quiet',
            audio_url
        ]
        self.__proc = subprocess.Popen(cmd)
        self.__status = PlayerStatus.PLAYING

    def stop(self):
        if self.__proc and self.__proc.poll() is None:
            self.__proc.terminate()
        self.__proc = None
        self.__status = PlayerStatus.STOPPED

    def set_current_url(self, url):
        self.current_url = url

    def get_status(self):
        return self.__status.label()


player = Player()
