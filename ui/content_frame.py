import tkinter as tk
from ui.header_frame import HeaderFrame
from ui.scrollable_frame import ScrollableFrame
from ui.form_frame import FormFrame


class ContentFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="white", width=458, height=800)
        self.view()

    def view(self):
        header_frame = HeaderFrame(self)
        header_frame.pack(fill=tk.BOTH)

        scrollable_frame = ScrollableFrame(self)
        scrollable_frame.pack(fill=tk.BOTH)

        form_frame = FormFrame(self)
        form_frame.pack(fill=tk.BOTH)
