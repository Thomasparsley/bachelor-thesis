import re
import tkinter as tk

INDEX = "1.0"


def add_tag(widget: tk.Text, tag_name: str, word: str, regex=None):
    """Add tags with 'tag_name' into widget by specific word or regex"""

    index = INDEX
    while True:
        # Search in widget for specific word or regex
        if regex is not None:
            index = widget.search(
                f"{word}", index, nocase=False, stopindex=tk.END)
        else:
            index = widget.search(f"\y{word}\y", index,
                                  nocase=False, stopindex=tk.END, regexp=True)

        # If nothing is found, break
        if not index:
            break

        str_index = index + "+" + str(len(f"{word}")) + "c"

        print(index)
        print(str_index)

        widget.tag_add(tag_name, index, str_index)
        index = str_index


def set_tag_name(name: str) -> str:
    """'hc_' is appended to the 'name'"""

    return f"hc_{name}"


def by_word(widget: tk.Text, word: str, color: str):
    """Highlight widget by color with specific word"""

    tag_name = set_tag_name(word)

    widget.tag_remove(tag_name, INDEX, tk.END)
    add_tag(widget, tag_name, word)

    widget.tag_config(tag_name, foreground=color)


def by_regex(widget: tk.Text, pattern, color: str):
    """Highlight widget by color with regex"""

    tag_name = set_tag_name(pattern)

    widget_data = widget.get(float(INDEX), tk.END)
    regex = re.compile(rf"{pattern}", re.MULTILINE)

    widget.tag_remove(tag_name, INDEX, tk.END)

    for match in regex.finditer(widget_data):
        print(match.group())
        """ add_tag(widget, tag_name, match, regex=pattern) """

    widget.tag_config(tag_name, foreground=color)


def functions(widget: tk.Text, color: str):
    by_regex(
        widget, "[a-zA-Z0-9]+\(+[\w\s,]+\)|[a-zA-Z0-9]+\(\)", color)


def comments(widget: tk.Text, color: str):
    by_regex(widget, r"\/\/.*", color)
    by_regex(widget, r"\/\*.*?[\r\n]*\*\/", color)
