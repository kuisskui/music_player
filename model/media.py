import json
import os
import tempfile
from yt_dlp import YoutubeDL


class Media:
    CACHE_FILE = os.path.join(tempfile.gettempdir(), "media_cache.json")

    def __init__(self, audio_path: str, name: str, url: str):
        self.__path = audio_path
        self.__name = name
        self.__url = url

    @classmethod
    def build(cls, url: str) -> "Media":
        if os.path.exists(cls.CACHE_FILE):
            with open(cls.CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
        else:
            cache = {}

        entry = cache.get(url)
        if entry and os.path.exists(entry["path"]):
            return cls(entry["path"], entry["title"], url)

        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True,
            "noplaylist": True,
            "outtmpl": os.path.join(tempfile.gettempdir(), "%(id)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            base = ydl.prepare_filename(info).rsplit(".", 1)[0]
            audio_path = base + ".mp3"
            title = info.get("title", info.get("id"))

        cache[url] = {"path": audio_path, "title": title}
        with open(cls.CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)

        return cls(audio_path, title, url)

    def get_path(self) -> str:
        return self.__path

    def get_name(self) -> str:
        return self.__name

    def get_url(self) -> str:
        return self.__url
