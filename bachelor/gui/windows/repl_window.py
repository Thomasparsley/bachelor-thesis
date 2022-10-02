import tkinter as tk

from ..frames.repl import REPL
from ..widgets.textpeer import TextPeer


class REPLWindow:
    def __init__(self, root: tk.Misc | None, editor_master: tk.Text):
        self.window = tk.Toplevel(root)
        self.window.title("Duplicated REPL")

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.textpeer = TextPeer(self.window, editor_master)

        self.editor = REPL(self.window)
        self.editor.set_peer(editor_master)
        self.editor.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
