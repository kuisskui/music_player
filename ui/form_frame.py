import tkinter as tk
from model.media import Media
from model.player import player
from ui.card_frame import CardFrame



class FormFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(bg='white')
        self.view()

    def view(self):
        tk.Label(self,
                 text="Paste a youtube link",
                 bg="white", fg="black",
                 font=("Arial", 10)) \
            .pack(anchor="w", padx=10, pady=(10, 2))

        self.entry = tk.Entry(self, fg="gray", bg="white", font=("Arial", 12), bd=1, relief="solid", highlightthickness=0)
        self.entry.insert(0, "Link")
        self.entry.pack(fill="x", padx=10, pady=(0, 10))

        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._add_placeholder)
        self.entry.bind("<Return>", self._push_media)
        self.entry.bind("<Control-v>", lambda e: self.entry.event_generate("<<Paste>>"))

    def _clear_placeholder(self, event):
        if self.entry.get() == "Link":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def _add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Link")
            self.entry.config(fg="gray")

    def _push_media(self, event):
        url = self.entry.get()
        media = Media.build(url)
        player.get_playlist().add_media(media)
        # inner = app.content_frame.scrollable_frame.inner
        inner = self.master.scrollable_frame.inner
        card = CardFrame(media, inner)
        card.pack(fill="both", padx=10, pady=10)
