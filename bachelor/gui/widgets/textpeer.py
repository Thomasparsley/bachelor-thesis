import tkinter as tk

from ..types import StrDict


class TextPeer(tk.Text):
    """
    Text widget that connects to the data of another text widget.

    """

    def __init__(
        self,
        root: tk.Misc | None,
        master: "tk.Text",
        cnf: StrDict = {},
        **kwargs: StrDict
    ):
        super().__init__(root, cnf, **kwargs)
        self.destroy()
        master.peer_create(self, cnf)  # type: ignore
