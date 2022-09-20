import tkinter as tk

from .editor import Editor


class REPL(Editor):
    def __init__(self, root: tk.Tk | tk.Toplevel):
        super().__init__(root)

        self.input_count: int = 0

        self.text.insert(tk.END, f"{self.input_count} > ")
