import tkinter as tk
from tkinter import ttk
from widget import ScrollableFrame

class PlayingApp(tk.Tk):
    PLACEHOLDER = "Link"

    def __init__(self):
        super().__init__()
        self.title("Playing")
        # self.geometry("400x650")
        self.configure(bg="#888888")  # gray “margins”

        # ——— Content panel ———
        content = tk.Frame(self, bg="white", width=360, height=600)
        content.pack()

        # ——— Header ———
        header = tk.Frame(content, bg="black", height=50)
        header.pack(fill="x")
        tk.Label(header, text="Playing",
                 bg="black", fg="white",
                 font=("Arial", 16, "bold")) \
            .pack(side="left", padx=10, pady=10)
        tk.Label(header, text="กลับมาทำไม...หา",
                 bg="black", fg="white",
                 font=("Arial", 12)) \
            .pack(side="right", padx=10, pady=10)

        # ——— Card ———
        card = tk.Frame(content,
                        bg="white",
                        bd=1,
                        relief="solid")
        card.pack(fill="x", padx=10, pady=20)
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

        sf = ScrollableFrame(content)
        sf.pack(fill="both", expand=True)

        # Populate with many items
        for i in range(50):
            ttk.Label(sf.inner, text=f"Item {i + 1}").pack(pady=2, padx=5, anchor="w")

        # ——— Form Field ———
        tk.Label(content,
                 text="Paste a youtube link",
                 bg="white", fg="black",
                 font=("Arial", 12)) \
            .pack(anchor="w", padx=10, pady=(0, 5))

        self.entry = tk.Entry(content, fg="gray", font=("Arial", 11))
        self.entry.insert(0, self.PLACEHOLDER)
        self.entry.pack(fill="x", padx=10)

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
    app = PlayingApp()
    app.mainloop()
