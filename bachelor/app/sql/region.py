from .index import Index


class Region:
    __slots__ = "start", "end"

    def __init__(self, start: Index, end: Index) -> None:
        self.start = start
        self.end = end

    @classmethod
    def from_nums(cls, start_line: int, start_char: int, end_line: int, end_char: int):
        start = Index(start_line, start_char)
        end = Index(end_line, end_char)

        return cls(start, end)
