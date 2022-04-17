import tkinter as tk

from typing import List


class ButtonList(tk.Frame):
    def __init__(
        self,
        root: "tk.Tk", 
        side,
        buttons: "List",
    ):
        super().__init__(root)

        for button in buttons:
            btn = tk.Button(self,
                            text=button["text"], command=button["command"])
            btn.pack(side=side)
