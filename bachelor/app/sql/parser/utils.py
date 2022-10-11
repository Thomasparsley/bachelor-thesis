from ..enum import StatementVariant
from ..const import (
    NEW_LINES,
    SQL_WILDCARD,
    START_COMMENT,
    END_COMMENT,
)


def is_start_comment(input_: str) -> bool:
    """
    Returns whether the given input is a start comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a start comment.

    Examples:
        >>> is_start_comment("--")
        True

        >>> is_start_comment("/*")
        True

        >>> is_start_comment("/* --")
        False

        >>> is_start_comment("-- /*")
        False
    """
    return input_ in START_COMMENT


def is_end_comment(input_: str) -> bool:
    """
    Returns whether the given input is an end comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is an end comment.

    Examples:
        >>> is_end_comment("*/")
        True

        >>> is_end_comment("--")
        False

        >>> is_end_comment("/*")
        False
    """
    return input_ in END_COMMENT


def is_new_line(input_: str) -> bool:
    """
    Returns whether the given input is a new line.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a new line.

    Examples:
        >>> is_new_line("\\n")
        True

        >>> is_new_line("\\r\\n")
        True

        >>> is_new_line("\\r")
        False

        >>> is_new_line("\\n\\r")
        False

        >>> is_new_line("\\r\\n\\n")
        False

    """
    return input_ in NEW_LINES


def is_single_line_comment(input_: str) -> bool:
    """
    Returns whether the given input is a single line comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a single line comment.

    Examples:
        >>> is_single_line_comment("--\\n")
        True

        >>> is_single_line_comment("--")
        False

        >>> is_single_line_comment("/*")
        False

        >>> is_single_line_comment("/* --\\n")
        False

        >>> is_single_line_comment("-- /*\\n")
        True

        >>> is_single_line_comment("--Single Line Comment /*\\n")
        True
    """
    return input_[0:2] == START_COMMENT[0] and is_new_line(input_[len(input_) - 1])


def is_multi_line_comment(input_: str) -> bool:
    """
    Returns whether the given input is a multi line comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a multi line comment.

    Examples:
        >>> is_multi_line_comment("/* Multi Line Comment */")
        True

        >>> is_multi_line_comment("/*")
        False

        >>> is_multi_line_comment("/* --")
        False

        >>> is_multi_line_comment("-- /*")
        False
    """
    l = len(input_)
    return is_start_comment(input_[0:2]) and is_end_comment(input_[l - 2 : l])


def is_comment(input_: str) -> bool:
    """
    Returns whether the given input is a comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a comment.

    Examples:
        >>> is_comment("--\\n")
        True

        >>> is_comment("-- Is Single Line Comment\\n")
        True

        >>> is_comment("/* Is Multi Line Comment */")
        True

        >>> is_comment("/*")
        false

        >>> is_comment("/* --")
        False

        >>> is_comment("-- /*")
        False
    """
    return is_single_line_comment(input_) or is_multi_line_comment(input_)


def is_wildcard(input_: str) -> bool:
    return input_ == SQL_WILDCARD


def get_char(idx: int, statement: str) -> str:
    return statement[idx]


def peek(idx: int, statement: str):
    next_idx = idx + 1

    if next_idx >= len(statement):
        return ""

    return get_char(next_idx, statement)


def add_to_buffer(buff: str, char: str) -> str:
    return f"{buff}{char.lower()}"


def find_statement_variant(statement: str):
    idx = 0
    buff = ""

    while idx < len(statement):
        char = get_char(idx, statement)

        buff = add_to_buffer(buff, char)

        if StatementVariant.has_value(buff):
            return StatementVariant(buff)

        idx += 1

    return None
