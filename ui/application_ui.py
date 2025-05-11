import tkinter as tk
from scrollable_frame import ScrollableFrame
from content_frame import ContentFrame


class ApplicationUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music player")

        content_frame = ContentFrame(self)
        content_frame.pack()


if __name__ == "__main__":
    app = ApplicationUI()
    app.mainloop()
