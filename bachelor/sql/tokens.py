from enum import Enum


class Token(int, Enum):
    """
    Enum for SQL syntax.
    """
    KEYWORD: int = 1
    COMMENT: int = 2
    NUMBER: int = 3
    STRING: int = 4

    @property
    def color(self) -> str:
        match self:
            case Token.KEYWORD:
                return 'blue'
            case Token.COMMENT:
                return 'green'
            case Token.NUMBER:
                return 'green'
            case Token.STRING:
                return 'orange'
