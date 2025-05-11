import tkinter as tk


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
            .pack(anchor="w", padx=10, pady=(0, 5))

        self.entry = tk.Entry(self, fg="gray", font=("Arial", 12), bd=1, relief="solid", highlightthickness=0)
        self.entry.insert(0, "Link")
        self.entry.pack(fill="x", padx=10, pady=10)
        # placeholder handlers
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self.entry.get() == "Link":
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def _add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Link")
            self.entry.config(fg="gray")
