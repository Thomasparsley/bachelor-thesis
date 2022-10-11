from typing import Final


SQL_KEYWORDS: Final = (
    "SELECT",
    "FROM",
    "WHERE",
    "AND",
    "OR",
    "LIKE",
    "IN",
    "IS",
    "NULL",
    "NOT",
    "TRUE",
    "FALSE",
    "DISTINCT",
    "ALL",
    "AS",
    "ASC",
    "DESC",
    "ORDER",
    "BY",
    "GROUP",
    "HAVING",
    "LIMIT",
    "OFFSET",
    "INTO",
    "VALUES",
    "DUPLICATE",
    "KEY",
    "PRIMARY",
    "UNIQUE",
    "CHECK",
    "CONSTRAINT",
)

SQL_MACROS: Final = ("SYMDIFF",)
SQL_WILDCARD: Final = "*"

SPACE_CHAR: Final = " "
NEW_LINES: Final = ("\n", "\r\n")
EMPTY_CHARS: Final = (SPACE_CHAR, "\t", "\r", *NEW_LINES)

START_COMMENT: Final = ("--", "/*")
END_COMMENT: Final = "*/"

LEFT_PARENTHESIS: Final = "("
RIGHT_PARENTHESIS: Final = ")"
PARENTHESES: Final = (LEFT_PARENTHESIS, RIGHT_PARENTHESIS)
