import tkinter as tk
from ui.content_frame import ContentFrame


class ApplicationUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music player")

        self.content_frame = ContentFrame(self)
        self.content_frame.pack()
        self.bind_class(".", "<Tab>", self.on_tab)
        self.bind_class(".", "<space>", self.content_frame.header_frame.on_click)

    def on_tab(self, event):
        self.content_frame.form_frame.entry.focus_set()
        return "break"

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
