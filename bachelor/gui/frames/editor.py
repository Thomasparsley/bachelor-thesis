from typing import Any, Callable

import tkinter as tk
from sqlparse import format as sql_format  #   type: ignore

from ..utils.index import Index
from ..utils.events import events_caller
from ..widgets.textpeer import TextPeer


class Editor(tk.Frame):
    def __init__(self, root: tk.Tk | tk.Toplevel):
        super().__init__(root)

        self._keypress_events: list[Callable[[Any], Any]] = []
        self._keyrelease_events: list[Callable[[Any], Any]] = []

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.text = tk.Text(self)
        self._bind_events()

        self._layout_init()

    def _layout_init(self):
        self.text.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    def _bind_events(self):
        self.text.bind("<KeyPress>", self._keypress_events_caller)
        self.text.bind("<KeyRelease>", self._keyrelease_events_caller)

    def add_keypress_event(self, event: Callable[[Any], Any]):
        self._keypress_events.append(event)

    def _keypress_events_caller(self, event: Any = None):
        return events_caller(self._keypress_events, event)

    def add_keyrelease_event(self, event: Callable[[Any], Any]):
        self._keyrelease_events.append(event)

    def _keyrelease_events_caller(self, event: Any = None):
        return events_caller(self._keyrelease_events, event)

    @property
    def cursor_index(self):
        return Index.from_str(self.text.index(tk.INSERT))

    def get_data(self) -> str:
        return self.text.get("1.0", tk.END)

    def set_peer(self, master: tk.Text):
        self.text.destroy()
        self.text = TextPeer(self, master)
        self._bind_events()
        self._layout_init()

    def format(self):
        tmp = self.text.get("1.0", tk.END)
        self.text.delete("1.0", tk.END)

        self.text.insert(
            tk.END,
            sql_format(
                tmp,
                reindent=True,
                keyword_case="upper",
                use_space_around_operators=True,
            ),
        )
