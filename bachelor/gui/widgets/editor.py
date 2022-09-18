import tkinter as tk

from ..widgets.textpeer import TextPeer


class Editor(tk.Frame):
    def __init__(self, root: tk.Tk | tk.Toplevel):
        super().__init__(root, highlightbackground="blue", highlightthickness=1)

        self.paned_window = tk.PanedWindow(self, orient=tk.VERTICAL)

        self.text = tk.Text(self)
        # self.textarea.bind(
        #    "<KeyRelease>", lambda e: highlighter.highlight(self.textarea)
        # )
        self._text_layout_init()

        self.paned_window.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    def _text_layout_init(self):
        self.text.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.paned_window.add(self.text)  # type: ignore

    def get_data(self) -> str:
        return self.text.get("1.0", tk.END)

    def set_peer(self, master: tk.Text):
        self.text.destroy()
        self.text = TextPeer(self, master)
        self._text_layout_init()
