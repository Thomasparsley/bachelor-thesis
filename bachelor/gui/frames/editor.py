from typing import Any, Callable

import tkinter as tk

from ..utils.index import Index
from ..widgets.textpeer import TextPeer


class Editor(tk.Frame):
    def __init__(self, root: tk.Tk | tk.Toplevel):
        super().__init__(root)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.var = tk.StringVar()
        self.text = tk.Text(self)
        self.text.bind("<KeyPress>", self._text_keypress_events_caller)
        self.text.bind("<KeyRelease>", self._text_keyrelease_events_caller)

        self._keypress_events: list[Callable[[Any], Any]] = []
        self._keyrelease_events: list[Callable[[Any], Any]] = []

        # self.textarea.bind(
        #    "<KeyRelease>", lambda e: highlighter.highlight(self.textarea)
        # )
        self._layout_init()

    def _layout_init(self):
        self.text.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    @property
    def cursor_index(self):
        return Index.from_str(self.text.index(tk.INSERT))

    def get_data(self) -> str:
        return self.text.get("1.0", tk.END)

    def set_peer(self, master: tk.Text):
        self.text.destroy()
        self.text = TextPeer(self, master)
        self._layout_init()

    def add_keypress_event(self, event: Callable[[Any], Any]):
        self._keypress_events.append(event)

    def add_keyrelease_event(self, event: Callable[[Any], Any]):
        self._keyrelease_events.append(event)

    def _text_keypress_events_caller(self, event: Any = None):
        for e in self._keypress_events:
            result = e(event)
            if result == "break":
                return result

        return None

    def _text_keyrelease_events_caller(self, event: Any = None):
        for e in self._keyrelease_events:
            result = e(event)
            if result == "break":
                return result

        return None


class EditorFrame(Editor):
    def _format(self, widget: "tk.Text"):
        """
        Format function for format button.
        """
        temp = widget.get("1.0", tk.END)
        widget.delete("1.0", tk.END)

        widget.insert(
            tk.END,
            sqlparse.format(  # type: ignore
                temp,
                reindent=True,
                keyword_case="upper",
                use_space_around_operators=True,
            ),
        )
        # highlighter.highlight(widget)
