import tkinter as tk
from model.player import player
from model.media import Media
from model.player_status import PlayerStatus


class HeaderFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="black")
        self.view()

        self.bind("<Button-1>", self.on_click)

        for child in self.winfo_children():
            child.bind("<Button-1>", self.on_click)

    def view(self):
        tk.Label(self, text=player.get_status(),
                 bg="black", fg="white",
                 font=("Arial", 16, "bold")) \
            .pack(side="top", anchor="w", padx=14, pady=14)

        tk.Label(self, text="กลับมาทำไม...หา",
                 bg="black", fg="white",
                 font=("Arial", 12)) \
            .pack(side="bottom", anchor="e", padx=14, pady=14)

    def on_click(self, event):
        if player.get_status() is PlayerStatus.PLAYING:
            player.stop()
        else:
            player.play(Media(player.current_url))
