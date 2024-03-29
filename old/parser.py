from typing import List

from .region import Region
from .tokens import Token
from .keywords import KEYWORDS

NEW_LINES = ["\n", "\r\n"]
EMPTY_CHARS = [" ", "\t", "\r", *NEW_LINES]

START_COMMENT = ["--", "/*"]
END_COMMENT = ["*/"]


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


def is_empty_char(input_: str) -> bool:
    """
    Returns whether the given input is an empty char.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is an empty char.
    """
    return input_ in EMPTY_CHARS


def is_number(input_: str) -> bool:
    """
    Returns whether the given input is a number.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a number.

    Examples:
        >>> is_number("1")
        True

        >>> is_number("1.0")
        True

        >>> is_number("-1")
        True

        >>> is_number("a")
        False
    """
    try:
        float(input_)
        return True
    except:
        return False


def is_keyword(input: str) -> bool:
    """
    Returns whether the given input is a SQL keyword.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a SQL keyword.

    Examples:
        >>> is_keyword("SELECT")
        True

        >>> is_keyword("select")
        False
    """
    return input in KEYWORDS


def is_string(input_: str) -> bool:
    """
    Returns whether the given input is a string.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a string.

    Examples:
        >>> is_string("'string'")
        True

        >>> is_string("'string")
        False

        >>> is_string("string")
        False

        >>> is_string("'")
        False

        >>> is_string("''")
        True
    """
    l = len(input_)

    if l < 2:
        return False

    return input_[0] == "'" and input_[len(input_) - 1] == "'"


def parse(text: str) -> List["Region"]:
    """
    Parses the given text and returns a list of regions for highlighting.

    Args:
        text (str): The text to parse.

    Returns:
        list[Region]: A list of regions.

    Examples:
        >>> parse("SELECT * FROM table; -- Comment")
        [<Region object at ...>, <Region object at ...>, <Region object at ...>]
    """
    next_region: "Region" = None
    regions: List["Region"] = []

    buff = ""
    comment_buff = ""

    n_of_chars = 0
    n_of_lines = 1

    text_len = len(text)
    idx = 0

    while idx < text_len:
        char = text[idx]

        if is_new_line(char):
            n_of_lines += 1
            n_of_chars = 0
            buff = ""
        else:
            n_of_chars += 1

            buff += char
            if char == " ":
                buff = ""
            if char == ";":
                buff = ""
                idx += 1
                continue

        # region Comments
        if is_start_comment(text[idx - 1 : idx + 1]) and comment_buff == "":
            next_region = Region(
                n_of_lines, n_of_chars - 2, len(comment_buff), Token.COMMENT
            )
            comment_buff += text[idx - 1 : idx + 1]
            buff = ""

            idx += 1
            continue

        if comment_buff:
            comment_buff += char
            next_region.region_len = len(comment_buff)

            if is_comment(comment_buff):
                regions.append(next_region)
                next_region = None

                comment_buff = ""
                idx += 1
                continue
        # endregion

        if not is_empty_char(text[idx]) and is_empty_char(text[idx + 1]):
            if is_number(buff):
                regions.append(
                    Region(n_of_lines, n_of_chars - len(buff), len(buff), Token.NUMBER)
                )
                buff = ""
                idx += 1
                continue

            if is_string(buff):
                regions.append(
                    Region(n_of_lines, n_of_chars - len(buff), len(buff), Token.STRING)
                )
                buff = ""
                idx += 1
                continue

            if is_keyword(buff):
                regions.append(
                    Region(n_of_lines, n_of_chars - len(buff), len(buff), Token.KEYWORD)
                )
                buff = ""
                idx += 1
                continue

        idx += 1

    if next_region:
        regions.append(next_region)

    return regions
