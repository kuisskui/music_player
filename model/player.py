import subprocess
import time

from model.player_status import PlayerStatus
from model.playlist import Playlist


class Player:
    _instances = {}

    def __init__(self):
        self.__proc = None
        self.__status: PlayerStatus = PlayerStatus.READY
        self.__pointer = 0
        self.__start_time = 0
        self.__paused_offset = 0
        self.__playlist: Playlist = Playlist("New Playlist", [])

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def play(self, start: float = 0.0):
        self.stop()
        self.__status = PlayerStatus.LOADING
        self.__start_time = time.monotonic() - start

        cmd = ['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', '-i',
               self.__playlist.get_media(0).get_audio_url(), '-ss', str(start)]
        print(cmd)

        self.__proc = subprocess.Popen(cmd)
        self.__status = PlayerStatus.PLAYING

    def resume(self):
        self.play(self.__paused_offset)

    def stop(self):
        if self.__proc and self.__proc.poll() is None:
            elapsed = time.monotonic() - self.__start_time
            self.__paused_offset = elapsed
            self.__proc.terminate()

        self.__proc = None
        self.__status = PlayerStatus.STOPPED

    def get_status(self):
        return self.__status

    def get_playlist(self):
        return self.__playlist

    def get_pointer(self):
        return self.__pointer

    def set_pointer(self, pointer):
        self.__pointer = pointer


player = Player()
