import tkinter as tk


class CardFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="white", bd=1, relief=tk.SOLID)
        self.view()

    def view(self):
        tk.Label(self, text="Title",
                 bg="white", fg="black",
                 font=("Arial", 14, "bold")) \
            .pack(anchor="w", padx=10, pady=(10, 0))

        tk.Label(self,
                 text="Body text for whatever you’d like to say. "
                      "Add main takeaway points, quotes, anecdotes.",
                 bg="white", fg="#666666",
                 wraplength=320, justify="left",
                 font=("Arial", 10)) \
            .pack(anchor="w", padx=10, pady=(5, 10))
