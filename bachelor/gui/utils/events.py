from typing import Any, Callable


def events_caller(
    events: list[Callable[[Any], Any]],
    event: Any = None,
):
    for e in events:
        result = e(event)
        if result == "break":
            return result

    return None
