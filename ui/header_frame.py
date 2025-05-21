import tkinter as tk
from model.player import player
from model.player_status import PlayerStatus


class HeaderFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.status_label = tk.Variable()
        self.title_label = tk.Variable()

        player.observe(self.status_label, lambda: player.get_status().label())
        player.observe(self.title_label, lambda: player.get_playlist().get_media(player.get_pointer()).get_name())

        self.view()

        self.configure(bg="black")
        self.__bind()
        self.after(500, self._check_end_of_track)

    def _check_end_of_track(self):

        if player.has_finished() and player.get_status() is PlayerStatus.playing:
            player.play_next()

        self.after(1000, self._check_end_of_track)

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
        player.toggle()

    def __bind(self):
        self.bind("<Button-1>", self.on_click)

        for child in self.winfo_children():
            child.bind("<Button-1>", self.on_click)
