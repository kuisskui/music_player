import tkinter as tk


class HeaderFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="black")
        self.view()

    def view(self):
        tk.Label(self, text="Playing...",
                 bg="black", fg="white",
                 font=("Arial", 16, "bold")) \
            .pack(side="top", anchor="w", padx=14, pady=14)

        tk.Label(self, text="กลับมาทำไม...หา",
                 bg="black", fg="white",
                 font=("Arial", 12)) \
            .pack(side="bottom", anchor="e", padx=14, pady=14)
