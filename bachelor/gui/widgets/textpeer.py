import tkinter as tk
from typing import Any


class TextPeer(tk.Text):
    """
    Text widget that connects to the data of another text widget.

    """

    def __init__(
        self,
        root: tk.Misc | None,
        master: "tk.Text",
        cnf: dict[str, Any] = {},
        **kwargs: dict[str, Any]
    ):
        super().__init__(root, cnf, **kwargs)
        self.destroy()
        master.peer_create(self, cnf)  # type: ignore
