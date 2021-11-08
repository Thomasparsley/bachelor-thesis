import time

import tkinter as tk

import highlighter as hlt
from sql import highligter, keywords


def highlighter(event):
    """ for w in keywords.KEYWORDS:
        hlt.by_word(text_editor, w, "blue")
        hlt.by_word(text_editor, w.lower(), "blue")

    # Find strings (e. g. 'John')
    hlt.by_regex(text_editor, r"'+[\w\s]+'", "orange")

    # Find numbers (e. g. 123)
    hlt.by_regex(text_editor, r"\s+[0-9]+", "green")

    hlt.functions(text_editor, "orange")
    hlt.comments(text_editor, "green") """

    highligter.highlight(text_editor)


root = tk.Tk()

text_editor = tk.Text(root)
text_editor.bind("<KeyRelease>", highlighter)
text_editor.pack()

root.mainloop()
