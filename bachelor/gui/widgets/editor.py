import tkinter as tk

from ..widgets.textpeer import TextPeer


class Editor(tk.Frame):
    def __init__(self, root: tk.Tk | tk.Toplevel, peer: TextPeer | None = None):
        super().__init__(root, highlightbackground="blue", highlightthickness=1)

        paned_window = tk.PanedWindow(self, orient=tk.VERTICAL)

        if peer:
            self.text = peer
        else:
            self.text = tk.Text(self)
            # self.textarea.bind(
            #    "<KeyRelease>", lambda e: highlighter.highlight(self.textarea)
            # )

        self.text.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        paned_window.add(self.text)  # type: ignore

        paned_window.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    def get_data(self) -> str:
        return self.text.get("1.0", tk.END)
