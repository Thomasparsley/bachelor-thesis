from ..enum import Keyword
from ..region import Region
from ..token import KeywordToken
from ..statement import SelectStatement
from ..const import PARENTHESES, SPACE_CHAR

from .utils import get_char, add_to_buffer


def parse_select_statement(statement: str):
    select_statement = SelectStatement()

    idx = 0
    buff: str = ""
    char: str = ""
    line_number = 1
    char_number = 0

    def next_cycle() -> None:
        nonlocal idx
        nonlocal char_number

        idx += 1
        char_number += 1

        """def new_line() -> None:
        nonlocal buff
        nonlocal line_number
        nonlocal char_number

        line_number += 1
        char_number = 0
        buff = """

    # Parse select token
    while idx < len(statement):
        char = get_char(idx, statement)

        if char == SPACE_CHAR:
            buff = ""
        elif char in PARENTHESES:
            buff = ""
        elif buff == Keyword.SELECT:
            select_token = KeywordToken()
            select_token.keyword = Keyword.SELECT
            select_token.region = Region.from_nums(
                line_number,
                char_number - len(Keyword.SELECT),
                line_number,
                char_number,
            )

        next_cycle()
        buff = add_to_buffer(buff, char)

        if "select_token" in vars():
            break

    if "select_token" in vars():
        select_statement.select = select_token  # type: ignore
    else:
        raise Exception("Keyword SELECT not found")

    # Parse result

    while idx < len(statement):
        char = get_char(idx, statement)

        if char == SPACE_CHAR:
            buff = ""

        next_cycle()
        buff = add_to_buffer(buff, char)

    return select_statement
