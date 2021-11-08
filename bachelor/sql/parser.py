from .region import Region
from .enum import SqlSyntaxEnum
from .keywords import KEYWORDS

NEW_LINES = ["\n", "\r\n"]
EMPTY_CHARS = [" ", "\t", "\r", *NEW_LINES]

START_COMMENT = ["--", "/*"]
END_COMMENT = ["*/"]


def is_start_comment(input: str) -> bool:
    """Returns whether the given input is a start comment.

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
    return input in START_COMMENT


def is_end_comment(input: str) -> bool:
    """Returns whether the given input is an end comment.

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
    return input in END_COMMENT


def is_single_line_comment(input: str) -> bool:
    """Returns whether the given input is a single line comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a single line comment.

    Examples:
        >>> is_single_line_comment("--\n")
        True

        >>> is_single_line_comment("--")
        False

        >>> is_single_line_comment("/*")
        False

        >>> is_single_line_comment("/* --\n")
        False

        >>> is_single_line_comment("-- /*\n")
        True

        >>> is_single_line_comment("--Single Line Comment /*\n")
        True
    """

    return input[0:2] == START_COMMENT[0] and is_new_line(input[len(input) - 1])


def is_multi_line_comment(input: str) -> bool:
    """Returns whether the given input is a multi line comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a multi line comment.

    Examples:
        >>> is_multi_line_comment("/* Multi Line Comment */")
        true

        >>> is_multi_line_comment("/*")
        False

        >>> is_multi_line_comment("/* --")
        False

        >>> is_multi_line_comment("-- /*")
        False
    """
    l = len(input)
    return is_start_comment(input[0:2]) and is_end_comment(input[l-2:l])


def is_comment(input: str) -> bool:
    """Returns whether the given input is a comment.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a comment.

    Examples:
        >>> is_comment("--\n")
        True

        >>> is_comment("-- Is Single Line Comment\n")
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
    return is_single_line_comment(input) or is_multi_line_comment(input)


def is_new_line(input: str) -> bool:
    """Returns whether the given input is a new line.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is a new line.

    Examples:
        >>> is_new_line("\n")
        True

        >>> is_new_line("\r\n")
        True

        >>> is_new_line("\r")
        False

        >>> is_new_line("\n\r")
        False

        >>> is_new_line("\r\n\n")
        False
    """
    return input in NEW_LINES


def is_empty_char(input: str) -> bool:
    """Returns whether the given input is an empty char.

    Args:
        input (str): The input to check.

    Returns:
        bool: Whether the given input is an empty char.
    """
    return input in EMPTY_CHARS


def is_number(input: str) -> bool:
    """Returns whether the given input is a number.

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
        if isinstance(float(input), float):
            return True
    except:
        return False


def is_keyword(input: str) -> bool:
    """Returns whether the given input is a SQL keyword.

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


def parse(text: str) -> list[Region]:
    """Parses the given text and returns a list of regions.

    Args:
        text (str): The text to parse.

    Returns:
        list[Region]: A list of regions.

    Examples:
        >>> parse("SELECT * FROM table; -- Comment")
        [<Region object at ...>, <Region object at ...>, <Region object at ...>]
    """
    next_region: Region = None
    regions: list[Region] = []

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

        # region Comments
        if is_start_comment(text[idx-1:idx+1]) and comment_buff == "":
            next_region = Region(n_of_lines, n_of_chars-2,
                                 len(comment_buff), SqlSyntaxEnum.COMMENT)
            comment_buff += text[idx-1:idx+1]
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

        if not is_empty_char(text[idx]) and is_empty_char(text[idx+1]):
            if is_number(buff):
                regions.append(Region(n_of_lines, n_of_chars-len(buff),
                                      len(buff), SqlSyntaxEnum.NUMBER))
                buff = ""
                idx += 1
                continue

            if is_keyword(buff) or is_number(buff):
                regions.append(Region(n_of_lines, n_of_chars-len(buff),
                                      len(buff), SqlSyntaxEnum.KEYWORD))
                buff = ""
                idx += 1
                continue

        idx += 1

    if next_region:
        regions.append(next_region)

    return regions
