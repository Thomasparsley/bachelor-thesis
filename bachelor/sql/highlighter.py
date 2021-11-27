import tkinter as tk

from .enum import SqlSyntaxEnum
from .region import Region
from .parser import parse


def highlight(widget: tk.Text):
    """Highlights the regions in the given text widget.

    Args:
        widget (tk.Text): The text widget to highlight.
    """
    regions = parse(widget.get("1.0", tk.END))

    for keyword_type in SqlSyntaxEnum:
        widget.tag_remove(Region.make_tag(keyword_type), "1.0", tk.END)

    for region in regions:
        widget.tag_add(region.tag(), region.start(), region.end())

    for keyword_type in SqlSyntaxEnum:
        tag = Region.make_tag(keyword_type)
        widget.tag_config(tag, foreground=keyword_type.color)
