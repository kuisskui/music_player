import tkinter as tk
from ui.content_frame import ContentFrame


class ApplicationUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music player")

        self.content_frame = ContentFrame(self)
        self.content_frame.pack()
        self.bind_class(".", "<Tab>", self.on_tab)

    def on_tab(self, event):
        self.content_frame.form_frame.entry.focus_set()
        return "break"


if __name__ == "__main__":
    app = ApplicationUI()
    app.mainloop()
