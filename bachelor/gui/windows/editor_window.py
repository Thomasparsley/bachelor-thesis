import tkinter as tk

from .window import Window
from ..frames.editor import Editor
from ..widgets.textpeer import TextPeer


class EditorWindow(Window):

    window_title: str = "Duplicated editor"

    def __init__(self, root: tk.Misc, editor_master: tk.Text):
        super().__init__(root)

        self.textpeer = TextPeer(self.window, editor_master)

        self.editor = Editor(self.window)
        self.editor.set_peer(editor_master)
        self.editor.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    def main_menu_layout(self):
        menu = tk.Menu(self.window)

        ###############
        # SQL Menu
        sql_menu = tk.Menu(menu, tearoff=0)
        sql_menu.add_command(label="Spustit vše")
        sql_menu.add_command(label="Spustit vybrané")
        sql_menu.add_separator()
        sql_menu.add_command(label="Formátovat", command=self._format_cmd)

        menu.add_cascade(label="SQL", menu=sql_menu)
        return menu

    def _format_cmd(self):
        self.editor.format()
