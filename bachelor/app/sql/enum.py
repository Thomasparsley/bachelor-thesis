from enum import Enum, IntEnum


class StrEnum(str, Enum):
    @classmethod
    def has_value(cls, value: str):
        return value in cls._value2member_map_


class Direction(StrEnum):
    ASC = "asc"
    DESC = "desc"


class Keyword(StrEnum):
    SELECT = "select"
    FROM = "from"


class StatementVariant(StrEnum):
    SELECT = "select"
    UPDATE = "update"


class TokenVariant(IntEnum):
    WILDCARD = 1
    TABLE = 2
    COLUMN = 3
    FUNCTION = 4
    OPERATION = 5
    ORDER = 6


class TokenOperation(IntEnum):
    LIKE = 1


class TokenFormat(IntEnum):
    BINARY = 1


class TokenType(IntEnum):
    IDENTIFIER = 1
    FUNCTION = 2
    EXPRESSION = 3
    KEYWORD = 4

    # @property
    # def color(self) -> str:
    #    match self:
    #        case TokenType.KEYWORD:
    #            return "blue"
    #        case TokenType.COMMENT:
    #            return "green"
    #        case TokenType.NUMBER:
    #            return "green"
    #        case TokenType.STRING:
    #            return "orange"
    #        case TokenType.WILDCARD:
    #            return "white"
