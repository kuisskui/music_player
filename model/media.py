from yt_dlp import YoutubeDL


class Media:
    def __init__(self, audio_url, name):
        self.__audio_url = audio_url
        self.__name = name

    @classmethod
    def build(cls, url):
        ydl_opts = {'format': 'bestaudio/best', 'quiet': True, 'noplaylist': True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        return Media(info['url'], info['title'])

    def get_audio_url(self):
        return self.__audio_url

    def get_name(self):
        return self.__name
