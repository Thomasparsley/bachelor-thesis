import tkinter as tk


class SqlEditorFrame(tk.Frame):
    def __init__(self, root: "tk.Tk"):
        super().__init__(root, highlightbackground="blue", highlightthickness=1)

        self._textarea()

    def textarea_data(self) -> str:
        return self.textarea.get("1.0", tk.END)

    def _textarea(self):
        self.textarea = tk.Text(self)
        # self.textarea.bind("<KeyRelease>",
        #                   lambda e: highlighter.highlight(self.textarea))
        self.textarea.pack(expand=True, fill=tk.BOTH)

    def _format(self, widget: "tk.Text"):
        """
        Format function for format button.
        """
        # temp = widget.get("1.0", tk.END)
        # widget.delete("1.0", tk.END)

        # widget.insert(tk.END,
        #              sqlparse.format(temp, reindent=True, keyword_case='upper',
        #                              use_space_around_operators=True))
        # highlighter.highlight(widget)
