import tkinter as tk

from model.media import Media


class CardFrame(tk.Frame):
    def __init__(self, media: Media, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="white", bd=1, relief=tk.SOLID)
        self.__media = media
        self.view()

    def view(self):
        tk.Label(self, text=self.__media.get_name(),
                 bg="white", fg="black",
                 font=("Arial", 14, "bold")) \
            .pack(anchor="w", padx=10, pady=(10, 0))

        tk.Label(self,
                 text=self.__media.get_audio_url(),
                 bg="white", fg="#666666",
                 wraplength=320, justify="left",
                 font=("Arial", 10)) \
            .pack(anchor="w", padx=10, pady=(5, 10))
