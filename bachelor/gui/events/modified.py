from typing import Any


class ModifiedEvent:
    def __init__(self):
        self.bind("<<modified>>", self._been_modified)  # type: ignore

    def _been_modified(self, event: Any = None):
        self.been_modified(event)

    def been_modified(self, event: Any = None):
        pass
