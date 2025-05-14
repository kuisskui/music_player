from yt_dlp import YoutubeDL
import os
import tempfile


class Media:
    def __init__(self, audio_path: str, name: str):
        self.__audio_path = audio_path
        self.__name = name

    @classmethod
    def build(cls, url: str) -> "Media":
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noplaylist': True,
            'outtmpl': os.path.join(tempfile.gettempdir(), '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            audio_path = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.mp3'
            title = info.get('title', info.get('id'))
            return cls(audio_path, title)

    def get_audio_url(self) -> str:
        return self.__audio_path

    def get_name(self) -> str:
        return self.__name
