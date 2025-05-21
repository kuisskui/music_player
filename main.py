import os
from model.media import Media
from ui.application_ui import ApplicationUI
from model.cache_manager import CacheManager
from model.player import player


if not os.path.exists(Media.CACHE_FILE):
    media = Media.build("https://www.youtube.com/watch?v=Alh4nsKYjS4")
    player.get_playlist().add_media(media)

cache_manager = CacheManager()
media_list = cache_manager.fetch_media()
player.get_playlist().add_medias(media_list)

applicationUI = ApplicationUI()
applicationUI.mainloop()
