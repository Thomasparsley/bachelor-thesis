import tkinter as tk

from ..widgets.editor import Editor


class EditorFrame(Editor):
    def _format(self, widget: "tk.Text"):
        """
        Format function for format button.
        """
        temp = widget.get("1.0", tk.END)
        widget.delete("1.0", tk.END)

        widget.insert(
            tk.END,
            sqlparse.format(  # type: ignore
                temp,
                reindent=True,
                keyword_case="upper",
                use_space_around_operators=True,
            ),
        )
        # highlighter.highlight(widget)
