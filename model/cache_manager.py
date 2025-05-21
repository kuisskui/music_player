import json
import os
import tempfile

from model.media import Media


class CacheManager:
    CACHE_FILE = os.path.join(tempfile.gettempdir(), "media_cache.json")

    def __init__(self):
        pass

    def fetch_media(self):
        media_list = []
        with open(self.CACHE_FILE, "r") as f:
            cache = json.load(f)
        for url, value in cache.items():
            media = Media(value['path'], value['title'], '')
            media_list.append(media)
        return media_list
