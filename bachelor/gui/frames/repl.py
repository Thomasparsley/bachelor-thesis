import tkinter as tk
from typing import Any

from .editor import Editor
from ..utils.index import Index


class REPL(Editor):
    def __init__(self, root: tk.Tk | tk.Toplevel):
        super().__init__(root)

        self.input_count: int = 0
        self.cursor_stop_index = Index(1, 4)

        self.text.insert(tk.END, f"{self.input_count} > ")
        self.add_keypress_event(self.content_protection)
        self.add_keyrelease_event(self.content_exec)

    def content_protection(self, event: Any = None):
        keysym: str = event.keysym

        # Pokud zmáčknutá klávesa je na pohyb v textu, vždy povolit
        if keysym in ["Left", "Right", "Up", "Down"]:
            return

        cursor_index = self.cursor_index
        cursor_stop_index = self.cursor_stop_index
        if cursor_index <= cursor_stop_index:
            if keysym in ["BackSpace"]:
                return "break"

        # Pokud zmáčknutá klávesa je dále než stop_cursor, povolit
        if cursor_index < cursor_stop_index:
            return "break"

        try:
            select_start = Index.from_str(self.text.index("sel.first"))
            select_end = Index.from_str(self.text.index("sel.last"))

            if select_start <= cursor_stop_index or select_end <= cursor_stop_index:
                return "break"
        except tk.TclError:
            pass

        return

    def content_exec(self, event: Any = None):
        content = self.text.get(str(self.cursor_stop_index), tk.END)

        if content[-3:] == "\n\n\n":
            self.text.insert(tk.END, f"{self.input_count} < ")
            self.text.insert(tk.END, content)
            self.text.delete(f"{tk.END} - 1 lines", f"{tk.END} + 1 chars")

            self.input_count += 1
            self.text.insert(tk.END, f"{self.input_count} > ")
            current_index = self.text.index(f"{tk.END} - 1 chars")
            self.cursor_stop_index = Index.from_str(current_index)
