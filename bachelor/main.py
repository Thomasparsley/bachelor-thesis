import tkinter as tk

import sqlparse

from sql import highlighter


def sql_editor(root: tk.Tk):
    # Likes like spaghetti code :(
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    buttons_frame = tk.Frame(frame)
    buttons_frame.pack(side=tk.LEFT, anchor=tk.N)

    textarea = tk.Text(frame)
    textarea.bind("<KeyRelease>",
                  lambda e: highlighter.highlight(textarea))
    textarea.pack(side=tk.RIGHT)

    # Format function for format button
    def format(widget: tk.Text) -> None:
        temp = widget.get("1.0", tk.END)
        widget.delete("1.0", tk.END)

        widget.insert(tk.END,
                      sqlparse.format(temp,
                                      reindent=True, keyword_case='upper', use_space_around_operators=True))
        highlighter.highlight(widget)

    # Change to class?
    buttons_data = [
        {
            "text": "Run All",
            "command": lambda: None,
        },
        {
            "text": "Format",
            "command": lambda: format(textarea),
        }
    ]

    for data in buttons_data:
        data = tk.Button(buttons_frame,
                         text=data["text"], command=data["command"])
        data.pack(side=tk.TOP)


def terminal(root: tk.Tk):
    frame = tk.Frame(root)
    frame.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    terminal_output = tk.Text(frame)
    terminal_output.grid(row=0, column=0, columnspan=2,
                         sticky=tk.W+tk.E+tk.N+tk.S)

    terminal_input_label = tk.Label(frame, text=">>>")
    terminal_input_label.grid(row=1, column=0)

    terminal_input = tk.Entry(frame)
    terminal_input.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)


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
