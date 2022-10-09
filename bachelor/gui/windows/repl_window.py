import tkinter as tk

from .window import Window
from ..frames.repl import REPL
from ..cons import STICKY_ALL_SIDES
from ..widgets.textpeer import TextPeer


class REPLWindow(Window):

    window_title: str = "Duplicated REPL"

    def __init__(self, root: tk.Misc, editor_master: tk.Text) -> None:
        super().__init__(root)

        self.textpeer = TextPeer(self.window, editor_master)

        self.editor = REPL(self.window)
        self.editor.set_peer(editor_master)
        self.editor.grid(row=0, column=0, sticky=STICKY_ALL_SIDES)
