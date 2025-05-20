import tkinter as tk
from ui.content_frame import ContentFrame
from model.player import player


class ApplicationUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.content_frame = None

        self.view()
        self.__bind()
        # self.debug()

    def view(self):
        self.title("Music player")
        self.content_frame = ContentFrame(self)
        self.content_frame.pack()

    def __bind(self):
        self.bind_class(".", "<Tab>", self.handle_tab)
        self.bind_class(".", "<Escape>", self.handle_escape)
        self.bind_class(".", "<space>", self.handle_space)
        self.bind_class(".", "<KeyPress-j>", self.handle_j)
        self.bind_class(".", "<KeyPress-l>", self.handle_l)
        self.bind_class(".", "<KeyPress-k>", self.handle_k)

    def handle_tab(self, event):
        self.content_frame.form_frame.entry.focus_set()
        return "break"

    def handle_escape(self, event):
        self.focus_set()

    def handle_space(self, event):
        self.content_frame.header_frame.on_click("en")

    def handle_j(self, event):
        # play previous music
        player.play_previous()

    def handle_l(self, event):
        # stop and play
        player.play_next()

    def handle_k(self, event):
        # play next music
        player.toggle()

    def debug(self):
        CANDIDATES = [
            "<MouseWheel>",  # Windows/macOS scroll
            "<Button-4>",  # X11 scroll up
            "<Button-5>",  # X11 scroll down
            "<Button>",  # any mouse button press
            "<ButtonPress>",  # same as above
            "<ButtonRelease>",
            "<KeyPress>",
            "<KeyRelease>",
            "<Motion>",
            "<Enter>",
            "<Leave>",
        ]
        for seq in CANDIDATES:
            self.bind_all(seq, lambda e, s=seq: logger(e, s))

        def logger(evt, seq):
            print(f"Sequence: {seq:12}  widget: {evt.widget}  delta/num: {getattr(evt, 'delta', evt.num)}")


if __name__ == "__main__":
    app = ApplicationUI()
    app.mainloop()
