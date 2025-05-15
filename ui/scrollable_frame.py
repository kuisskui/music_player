import tkinter as tk
from tkinter import ttk
from ui.card_frame import CardFrame


class ScrollableFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="white", borderwidth=0, highlightthickness=0, height=600)
        self.v_scroll = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.v_scroll.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.v_scroll.set)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.inner = tk.Frame(self.canvas, bg="white")
        self.inner_id = self.canvas.create_window((0, 0), window=self.inner)
        self.inner.bind("<Configure>", self._on_frame_configure)

        self.view()

    def view(self):
        # ——— Card ———
        # TODO load all mp3 form storage
        pass

    def _on_canvas_configure(self, event):
        # Force the inner window to fill the canvas’s width
        self.canvas.itemconfig(self.inner_id, width=event.width)

    def _on_frame_configure(self, event):
        # Update scroll region to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        delta = -1 * (event.delta // 120) if event.delta else event.num == 5 and 1 or -1
        self.canvas.yview_scroll(delta, "units")


# ——— Example usage ———
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")

    sf = ScrollableFrame(root)
    sf.pack(fill="both", expand=True)

    # Populate with many items
    for i in range(50):
        ttk.Label(sf.inner, text=f"Item {i + 1}").pack(pady=2, padx=5, anchor="w")

    root.mainloop()
