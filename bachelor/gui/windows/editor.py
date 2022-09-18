import tkinter as tk

from ..widgets.editor import Editor
from ..widgets.textpeer import TextPeer


class EditorWindow:
    def __init__(self, root: tk.Misc | None, editor_master: tk.Text):
        self.window = tk.Toplevel(root)
        self.window.title("Duplicated editor")

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        paned_window = tk.PanedWindow(self.window, orient=tk.VERTICAL)

        self.textpeer = TextPeer(self.window, editor_master)

        self.editor = Editor(self.window, self.textpeer)
        self.editor.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        paned_window.add(self.editor)  # type: ignore

        paned_window.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
