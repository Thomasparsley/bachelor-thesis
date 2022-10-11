from ..statement import Statement
from ..enum import StatementVariant

from .parser_select import parse_select_statement
from .utils import find_statement_variant


def parser(full_statement: str):
    ast: list[Statement] = []

    statements = full_statement.split(";")

    for statement in statements:
        statement_variant = find_statement_variant(statement)

        if not statement_variant:
            continue

        match statement_variant:
            case StatementVariant.SELECT:
                ast.append(parse_select_statement(statement))
            case StatementVariant.UPDATE:
                pass

    return ast


""" class Tokeniser:
    def __init__(self, sql_statement: str) -> None:
        self.tokens: list[Token] = []
        self.idx = 0
        self.statement = sql_statement
        self.statement_length = len(sql_statement)

    def __call__(self) -> list[Token]:

        buff = ""
        line_number = 1
        char_number = 0

        while self.idx < len(self):
            char = self.get_char()

            if char == SPACE_CHAR:
                buff = ""

            elif self.peek() in EMPTY_CHARS and buff in SQL_KEYWORDS:
                self.add_token(TokenType.KEYWORD, buff, line_number, char_number)

            self.idx += 1
            buff = f"{buff}{char}"

        return self.tokens

    def add_token(
        self,
        token_type: TokenType,
        value: str,
        line: int,
        char: int,
    ) -> None:
        region = Region(
            Index(line, char - len(value)),
            Index(line, char),
        )
        new_token = Token(token_type, value, region)

        self.tokens.append(new_token) """
