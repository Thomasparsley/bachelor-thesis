import tkinter as tk

from sql import highligter


def highlighter(event):
    highligter.highlight(text_editor)


root = tk.Tk()

# region SQL editor
run_sql = tk.Button(root, text="Run")
run_sql.grid(row=0, column=0)

run_all_sql = tk.Button(root, text="Run All")
run_all_sql.grid(row=1, column=0)

format_sql = tk.Button(root, text="Format")
format_sql.grid(row=2, column=0)

text_editor = tk.Text(root)
text_editor.bind("<KeyRelease>", highlighter)
text_editor.grid(row=0, rowspan=3, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
# endregion

terminal_output = tk.Text(root)
terminal_output.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E+tk.N+tk.S)


terminal_input_label = tk.Label(root, text=">>>")
terminal_input_label.grid(row=4, column=0)

terminal_input = tk.Entry(root)
terminal_input.grid(row=4, column=1, sticky=tk.W+tk.E+tk.N+tk.S)

footer_info_example = tk.Label(root, text="connected to: 127.0.0.1:8080    |\
    db server: postres    |    last query: 0ms    |    example info")
footer_info_example.grid(row=5, column=0, columnspan=2)

root.mainloop()
