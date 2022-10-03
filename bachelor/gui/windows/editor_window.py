import tkinter as tk

from ..frames.editor import Editor
from ..widgets.textpeer import TextPeer


class EditorWindow:
    def __init__(self, root: tk.Misc | None, editor_master: tk.Text):
        self.window = tk.Toplevel(root)
        self.window.title("Duplicated editor")

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.textpeer = TextPeer(self.window, editor_master)

        self.editor = Editor(self.window)
        self.editor.set_peer(editor_master)
        self.editor.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        # self._main_menu()

    def _main_menu(self):
        self.main_menu_bar = tk.Menu(self.window)

        ###############
        # SQL Menu
        sql_menu = tk.Menu(self.main_menu_bar, tearoff=0)
        sql_menu.add_command(label="Spustit vše")
        sql_menu.add_command(label="Spustit vybrané")

        sql_menu.add_separator()

        sql_menu.add_command(label="Formátovat")

        self.main_menu_bar.add_cascade(label="SQL", menu=sql_menu)
