from typing import Any

import tkinter as tk


class Window:

    window_title: str = "Window"

    def __init__(self, root: tk.Misc) -> None:
        self._root = root
        self.window = tk.Toplevel(root)
        self.set_title(self.window_title)

        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)

        self.init_main_menu()

    def set_title(self, title: str) -> None:
        self.window.title(title)

    def main_menu_layout(self) -> tk.Menu:
        menu = tk.Menu(self.window)
        return menu

    def set_main_menu(self, menu: tk.Menu) -> None:
        self._root.set_main_menu(menu)  # type: ignore

    def init_main_menu(self) -> None:
        def set_menu(_: Any) -> None:
            menu = self.main_menu_layout()
            self.set_main_menu(menu)

        self.window.bind("<FocusIn>", set_menu)
