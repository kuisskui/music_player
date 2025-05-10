import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # 1) Canvas + scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        self.v_scroll = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.v_scroll.set)

        # 2) The interior frame where you put your widgets
        self.inner = ttk.Frame(self.canvas)
        self.inner_id = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")

        # 3) Layout
        self.v_scroll.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # 4) Make scroll region update when inner frame grows
        self.inner.bind("<Configure>", self._on_frame_configure)

        # 5) Optional: allow mousewheel scrolling when over the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_frame_configure(self, event):
        # Update scrollregion to encompass the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        # Windows / MacOS / Linux delta differences
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
