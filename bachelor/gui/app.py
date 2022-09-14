import os
import tkinter as tk

from .sql_editor import SqlEditorFrame


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

    def _sql_editor_init(self) -> None:
        self._sql_editor_frame = SqlEditorFrame(self)
        self._sql_editor_frame.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
        self.paned_window.add(self._sql_editor_frame)  # type: ignore
