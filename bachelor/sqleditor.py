import tkinter as tk

import sqlparse

from buttonlist import ButtonList
from sql import highlighter


class SqlEditorFrame(tk.Frame):
    def __init__(self, root: 'tk.Tk'):
        super().__init__(root)

        self._textarea()
        self.__buttons__()

    def textarea_data(self) -> str:
        return self.textarea.get("1.0", tk.END)

    def _textarea(self):
        self.textarea = tk.Text(self)
        self.textarea.bind("<KeyRelease>",
                           lambda e: highlighter.highlight(self.textarea))
        self.textarea.pack(side=tk.RIGHT)

    def __buttons__(self):
        buttons_data = [
            {
                "text": "Run Selected",
                "command": lambda: self.event_generate("<<RunSelectedSql>>"),
            },
            {
                "text": "Run All",
                "command": lambda: self.event_generate("<<RunAllSql>>"),
            },
            {
                "text": "Format",
                "command": lambda: self._format(self.textarea),
            }
        ]

        self.buttons = ButtonList(self, tk.TOP, buttons_data)
        self.buttons.pack(side=tk.LEFT, anchor=tk.N)

    def _format(self, widget: 'tk.Text'):
        """Format function for format button."""
        temp = widget.get("1.0", tk.END)
        widget.delete("1.0", tk.END)

        widget.insert(tk.END,
                      sqlparse.format(temp, reindent=True, keyword_case='upper',
                                      use_space_around_operators=True))
        highlighter.highlight(widget)
