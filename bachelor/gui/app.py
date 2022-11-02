import tkinter as tk
from typing import Any

from app.db_driver.driver import SqliteDriver

from .frames.repl import REPL
from .frames.editor import Editor
from .cons import STICKY_ALL_SIDES
from .windows import EditorWindow, REPLWindow


class App(tk.Tk):

    _app_name = "Bachelor App"

    def __init__(self) -> None:
        super().__init__()

        self.title(self._app_name)

        self.con = SqliteDriver("./test_sqlite_db")

        self._init_layout()

        self.bind("<FocusIn>", self._set_default_main_menu_event)

    def _init_layout(self) -> None:
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.paned_window = tk.PanedWindow(orient=tk.VERTICAL)

        self._editor_init()
        self._repl_init()

        self.paned_window.grid(row=0, column=0, sticky=STICKY_ALL_SIDES)

        self._main_menu()

    def _main_menu(self) -> None:
        self.set_default_main_menu()

    def _editor_init(self) -> None:
        self._editor = Editor(self)
        self._editor.grid(row=0, column=0, sticky=STICKY_ALL_SIDES)
        self.paned_window.add(self._editor)  # type: ignore

    def _repl_init(self) -> None:

        self._repl = REPL(self, self.con)
        self._repl.grid(row=1, column=0, sticky=STICKY_ALL_SIDES)
        self.paned_window.add(self._repl)  # type: ignore

    def _duplicate_editor(self) -> None:
        EditorWindow(self, self._editor.text)

    def _duplicate_repl(self) -> None:
        REPLWindow(self, self._repl.text, self.con)

    def _format_editor(self) -> None:
        self._editor.format()

    def set_main_menu(self, menu: tk.Menu) -> None:
        if hasattr(self, "_main_menu_bar"):
            self._main_menu_bar.destroy()

        self._main_menu_bar = menu
        self.config(menu=self._main_menu_bar)

    def _set_default_main_menu_event(self, _: Any) -> None:
        self.set_default_main_menu()

    def set_default_main_menu(self) -> None:
        menu = tk.Menu(self)

        ###########
        # File menu
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Novy", accelerator="Ctrl+N", underline=1)
        file_menu.add_command(label="Otevrit", accelerator="Ctrl+O", underline=1)
        file_menu.add_command(label="Ulozit", accelerator="Ctrl+S")
        file_menu.add_command(label="Ulozit jako", accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Ukoncit", command=self.quit, accelerator="Ctrl+Q")

        ##########
        # SQL Menu
        sql_menu = tk.Menu(menu, tearoff=0)
        sql_menu.add_command(label="Spustit vše")
        sql_menu.add_command(label="Spustit vybrané")
        sql_menu.add_separator()
        sql_menu.add_command(label="Formátovat", command=self._format_editor)

        ###############
        # Windows Menu
        windows = tk.Menu(menu, tearoff=0)
        windows.add_command(label="Duplicate editor", command=self._duplicate_editor)
        windows.add_command(label="Duplicate repl", command=self._duplicate_repl)

        menu.add_cascade(label="Soubor", menu=file_menu)
        menu.add_cascade(label="SQL", menu=sql_menu)
        menu.add_cascade(label="Windows", menu=windows)

        self.set_main_menu(menu)
