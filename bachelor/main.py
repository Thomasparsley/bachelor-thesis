import tkinter as tk

import sqlparse

from sql import highlighter


class ButtonList(tk.Frame):
    def __init__(self, root: tk.Tk,  side, buttons: list):
        super().__init__(root)

        for button in buttons:
            btn = tk.Button(self,
                            text=button["text"], command=button["command"])
            btn.pack(side=side)


class SqlEditorFrame(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root)

        self.textarea_frame()

        buttons_data = [
            {
                "text": "Run All",
                "command": lambda: None,
            },
            {
                "text": "Format",
                "command": lambda: format(self.textarea),
            }
        ]

        self.buttons = ButtonList(self, tk.TOP, buttons_data)
        self.buttons.pack(side=tk.LEFT, anchor=tk.N)

    def textarea_frame(self):
        self.textarea = tk.Text(self)
        self.textarea.bind("<KeyRelease>",
                           lambda e: highlighter.highlight(self.textarea))
        self.textarea.pack(side=tk.RIGHT)

    def __format__(self, widget: tk.Text):
        """Format function for format button."""
        temp = widget.get("1.0", tk.END)
        widget.delete("1.0", tk.END)

        widget.insert(tk.END,
                      sqlparse.format(temp, reindent=True, keyword_case='upper',
                                      use_space_around_operators=True))
        highlighter.highlight(widget)


class TerminalFrame(tk.Frame):
    def __init__(self, root: tk.Tk):
        super().__init__(root)

        self.__terminal_input__()
        self.__terminal_output__()

    def __terminal_input__(self):
        label = tk.Label(self, text=">>>")
        label.grid(row=1, column=0)

        entry = tk.Entry(self)
        entry.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

    def __terminal_output__(self):
        terminal_output = tk.Text(self)
        terminal_output.grid(row=0, column=0, columnspan=2,
                             sticky=tk.W+tk.E+tk.N+tk.S)


def sql_editor(root: tk.Tk):
    frame = SqlEditorFrame(root)
    frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)


def terminal(root: tk.Tk):
    frame = TerminalFrame(root)
    frame.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)


def footer(root: tk.Tk):
    frame = tk.Frame(root)
    frame.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    info = tk.Label(frame, text="connected to: 127.0.0.1:8080    |\
    db server: postres    |    last query: 0ms    |    example info")
    info.pack()


root = tk.Tk()

sql_editor(root)
terminal(root)
footer(root)

root.mainloop()
