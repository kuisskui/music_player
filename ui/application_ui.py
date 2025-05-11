import tkinter as tk
from scrollable_frame import ScrollableFrame


class ApplicationUI(tk.Tk):
    PLACEHOLDER = "Link"

    def __init__(self):
        super().__init__()
        self.title("Music player")

        # ——— Content panel ———
        content = tk.Frame(self, bg="white", width=360, height=800)
        content.pack()

        # ——— Header ———
        header = tk.Frame(content, bg="black", width=458, height=145)
        header.pack_propagate(False)
        header.pack()
        tk.Label(header, text="Playing...",
                 bg="black", fg="white",
                 font=("Arial", 16, "bold")) \
            .pack(side="top", anchor="w", padx=14, pady=14)

        tk.Label(header, text="กลับมาทำไม...หา",
                 bg="black", fg="white",
                 font=("Arial", 12)) \
            .pack(side="bottom", anchor="e", padx=14, pady=14)

        sf = ScrollableFrame(content)
        sf.pack(fill="both", expand=True)

        # ——— Card ———
        for _ in range(7):
            card = tk.Frame(sf.inner,
                            bg="white",
                            bd=1,
                            relief="solid")
            card.pack(fill="both", padx=10, pady=10)

            tk.Label(card, text="Title",
                     bg="white", fg="black",
                     font=("Arial", 14, "bold")) \
                .pack(anchor="w", padx=10, pady=(10, 0))

            tk.Label(card,
                     text="Body text for whatever you’d like to say. "
                          "Add main takeaway points, quotes, anecdotes.",
                     bg="white", fg="#666666",
                     wraplength=320, justify="left",
                     font=("Arial", 10)) \
                .pack(anchor="w", padx=10, pady=(5, 10))

        # ——— Form Field ———
        tk.Label(content,
                 text="Paste a youtube link",
                 bg="white", fg="black",
                 font=("Arial", 10)) \
            .pack(anchor="w", padx=10, pady=(0, 5))

        self.entry = tk.Entry(content, fg="gray", font=("Arial", 12), bd=1, relief="solid", highlightthickness=0)
        self.entry.insert(0, self.PLACEHOLDER)
        self.entry.pack(fill="x", padx=10, pady=10)

        # placeholder handlers
        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self.entry.get() == self.PLACEHOLDER:
            self.entry.delete(0, tk.END)
            self.entry.config(fg="black")

    def _add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.PLACEHOLDER)
            self.entry.config(fg="gray")


if __name__ == "__main__":
    app = ApplicationUI()
    app.mainloop()
