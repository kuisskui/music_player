import tkinter as tk
from model.player import player
from model.player_status import PlayerStatus


class HeaderFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.status_label = tk.Variable()
        self.title_label = tk.Variable()
        self.update()

        self.configure(bg="black")
        self.view()

        self.bind("<Button-1>", self.on_click)

        for child in self.winfo_children():
            child.bind("<Button-1>", self.on_click)

    def view(self):
        tk.Label(
            self, textvariable=self.status_label,
            bg="black", fg="white",
            font=("Arial", 16, "bold")
        ).pack(side="top", anchor="w", padx=14, pady=(14, 0))

        tk.Label(
            self, textvariable=self.title_label,
            bg="black", fg="white",
            font=("Arial", 12)
        ).pack(side="bottom", anchor="e", padx=14, pady=14)

    def on_click(self, event):
        if player.get_status() is PlayerStatus.PLAYING:
            player.stop()
        elif player.get_status() is PlayerStatus.STOPPED:
            player.resume()
        else:
            player.play()

        self.update()

    def update(self):
        self.status_label.set(player.get_status().label())
        self.title_label.set(player.get_playlist().get_media(player.get_pointer()).get_name())
