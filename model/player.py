import subprocess
import time
import tkinter as tk
from model.player_status import PlayerStatus
from model.playlist import Playlist


class Player:
    _instances = {}

    def __init__(self):
        self.__process = None
        self.__status: PlayerStatus = PlayerStatus.loading
        self.__pointer: int = 0
        self.__start_time: float = 0
        self.__paused_offset: float = 0
        self.__playlist: Playlist = Playlist("New Playlist", [])
        self.__observers = []
        self.set_status(PlayerStatus.ready)

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def has_finished(self) -> bool:
        return self.__process is not None and self.__process.poll() is not None

    def observe(self, tk_var: tk.Variable, getter):
        self.__observers.append((tk_var, getter))
        tk_var.set(getter())

    def notify_observers(self):
        for var, getter in self.__observers:
            var.set(getter())

    def play(self, start: float = 0.0):
        self.stop()
        self.set_status(PlayerStatus.loading)
        self.__start_time = time.monotonic() - start

        cmd = [
            'ffplay',
            '-nodisp',
            '-autoexit',
            '-loglevel', 'quiet',
            '-i', self.get_playlist().get_media(self.get_pointer()).get_path(),
            '-ss', f"{start:.6f}",
        ]

        self.__process = subprocess.Popen(cmd)
        self.set_status(PlayerStatus.playing)

    def resume(self):
        self.play(self.__paused_offset)

    def stop(self):
        if self.__process and self.__process.poll() is None:
            elapsed = time.monotonic() - self.__start_time
            self.__paused_offset = elapsed
            self.__process.terminate()

        self.__process = None
        self.set_status(PlayerStatus.stopped)

    def toggle(self):
        if self.get_status() is PlayerStatus.playing:
            self.stop()
        elif self.get_status() is PlayerStatus.stopped:
            self.resume()
        else:
            self.play()

    def play_next(self):
        self.stop()
        self.set_pointer(self.__pointer + 1)
        self.play()

    def play_previous(self):
        self.stop()
        self.set_pointer(self.__pointer - 1)
        self.play()

    def get_status(self):
        return self.__status

    def set_status(self, new: PlayerStatus):
        if new is not self.__status:
            self.__status = new
            self.notify_observers()

    def get_playlist(self):
        return self.__playlist

    def get_pointer(self):
        return self.__pointer

    def set_pointer(self, pointer):
        count_media = self.__playlist.count_media()
        if pointer < 0:
            pointer = count_media - 1
        elif pointer > count_media - 1:
            pointer = 0
        self.__pointer = pointer


player = Player()
