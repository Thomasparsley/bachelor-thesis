import tkinter as tk

from .frames.editor import EditorFrame
from .windows.editor import EditorWindow


class App(tk.Tk):

    _app_name = "Bachelor App"

    def __init__(self) -> None:
        super().__init__()

        self.title(self._app_name)

        self._init_layout()

    def _init_layout(self) -> None:
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.paned_window = tk.PanedWindow(orient=tk.VERTICAL)

        self._sql_editor_init()

        self.paned_window.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

        self._main_menu()
        self.config(menu=self._main_menu_bar)

    def _main_menu(self):
        self._main_menu_bar = tk.Menu(self)

        ###########
        # File menu
        file_menu = tk.Menu(self._main_menu_bar, tearoff=0)
        file_menu.add_command(label="Novy", accelerator="Ctrl+N", underline=1)
        file_menu.add_command(label="Otevrit", accelerator="Ctrl+O", underline=1)
        file_menu.add_command(label="Ulozit", accelerator="Ctrl+S")
        file_menu.add_command(label="Ulozit jako", accelerator="Ctrl+Shift+S")

        file_menu.add_separator()

        file_menu.add_command(label="Ukoncit", command=self.quit, accelerator="Ctrl+Q")

        self._main_menu_bar.add_cascade(label="Soubor", menu=file_menu)

        # Windows
        windows = tk.Menu(self._main_menu_bar, tearoff=0)
        windows.add_command(label="Duplicate editor", command=self._duplicate_editor)
        windows.add_command(label="Duplicate terminal")

        self._main_menu_bar.add_cascade(label="Windows", menu=windows)

    def _sql_editor_init(self) -> None:
        self._editor_frame = EditorFrame(self)
        self._editor_frame.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.paned_window.add(self._editor_frame)  # type: ignore

    def _duplicate_editor(self):
        EditorWindow(self, self._editor_frame.text)
