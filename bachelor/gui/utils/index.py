class Index:
    def __init__(self, line: int = 0, char: int = 0):
        self.line = line
        self.char = char

    @classmethod
    def from_str(cls, index: str):
        line, char = index.split(".")
        return cls(int(line), int(char))

    def __str__(self):
        return f"{self.line}.{self.char}"

    def __lt__(self, other: "Index") -> bool:
        if self.line < other.line:
            return True

        if self.line == other.line:
            if self.char < other.char:
                return True

        return False

    def __le__(self, other: "Index") -> bool:
        if self.line < other.line:
            return True

        if self.line == other.line:
            if self.char <= other.char:
                return True

        return False
