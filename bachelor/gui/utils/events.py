from typing import Any

from ..types import TkEvent


def events_caller(
    events: list[TkEvent],
    event: Any = None,
):
    for e in events:
        result = e(event)
        if result == "break":
            return result

    return None
