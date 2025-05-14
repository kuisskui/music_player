from model.media import Media


class Playlist:
    def __init__(self, name, media_list):
        self.name = name
        self.media_list: [Media] = media_list

    def add_media(self, media):
        self.media_list.append(media)

    def get_media(self, index) -> Media:
        if len(self.media_list) == 0:
            return Media("", "Empty playlist")
        return self.media_list[index]
