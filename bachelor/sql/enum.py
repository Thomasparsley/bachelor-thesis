from enum import Enum


class SqlSyntaxEnum(Enum):
    """Enum for SQL syntax."""
    KEYWORD = 1
    COMMENT = 2
    NUMBER = 3
    STRING = 4

    @property
    def color(self):
        match self:
            case SqlSyntaxEnum.KEYWORD:
                return 'blue'
            case SqlSyntaxEnum.COMMENT:
                return 'green'
            case SqlSyntaxEnum.NUMBER:
                return 'green'
            case SqlSyntaxEnum.STRING:
                return 'orange'
