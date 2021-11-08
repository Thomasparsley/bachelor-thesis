import tkinter as tk

from sql import highligter


def highlighter(event):
    highligter.highlight(text_editor)


root = tk.Tk()

text_editor = tk.Text(root)
text_editor.bind("<KeyRelease>", highlighter)
text_editor.pack()

root.mainloop()
