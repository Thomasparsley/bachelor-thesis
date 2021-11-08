import pytest

from bachelor.sql.enum import SqlSyntaxEnum
from bachelor.sql.region import Region
from bachelor.sql.parser import parse, is_start_comment, is_end_comment, \
    is_single_line_comment, is_multi_line_comment, is_comment, is_empty_char, \
    is_keyword, is_number

input = """SELECT * FROM user WHERE age = 96
/* Multi
Line
Comment */
-- Single Line Comment
asd asd asd user -- After
"""

parsed_output: list[Region] = parse(input)


@pytest.mark.parametrize(
    "id,test_input,expected_output",
    [
        # SELECT
        (1, parsed_output[0],
            Region(1, 0, 6, SqlSyntaxEnum.KEYWORD)),
        # FROM
        (2, parsed_output[1],
            Region(1, 9, 4, SqlSyntaxEnum.KEYWORD)),
        # WHERE
        (3, parsed_output[2],
            Region(1, 19, 5, SqlSyntaxEnum.KEYWORD)),
        # 96
        (4, parsed_output[3],
            Region(1, 31, 2, SqlSyntaxEnum.NUMBER)),
        # /* */
        (5, parsed_output[4],
            Region(2, 0, 24, SqlSyntaxEnum.COMMENT)),
        # --
        (6, parsed_output[5],
            Region(5, 0, 23, SqlSyntaxEnum.COMMENT)),
        # Key --
        (7, parsed_output[6],
            Region(6, 17, 9, SqlSyntaxEnum.COMMENT)),
    ],
)
def test_parser(id, test_input: Region, expected_output: Region):
    assert test_input.start_char == expected_output.start_char
    assert test_input.start_line == expected_output.start_line
    assert test_input.region_len == expected_output.region_len
    assert test_input.type == expected_output.type


@pytest.mark.parametrize(
    "id,test_input,expected_output",
    [
        # is_start_comment
        (0, is_start_comment("--"), True),
        (1, is_start_comment("/*"), True),
        (2, is_start_comment("/* --"), False),
        (3, is_start_comment("-- /*"), False),
        (4, is_start_comment("*/"), False),

        # is_end_comment
        (5, is_end_comment("*/"), True),
        (6, is_end_comment("/*"), False),
        (7, is_end_comment("--"), False),

        # is_single_line_comment
        (8, is_single_line_comment("--\n"), True),
        (9, is_single_line_comment("--"), False),
        (10, is_single_line_comment("/*"), False),
        (11, is_single_line_comment("/* --\n"), False),
        (12, is_single_line_comment("-- /*\n"), True),
        (13, is_single_line_comment("--Single Line Comment /*\n"), True),

        # is_multi_line_comment
        (14, is_multi_line_comment("/* Multi Line Comment */"), True),
        (15, is_multi_line_comment("/*"), False),
        (16, is_multi_line_comment("/* --"), False),
        (17, is_multi_line_comment("-- /*"), False),

        # is_comment
        (18, is_comment("--\n"), True),
        (19, is_comment("-- Is Single Line Comment\n"), True),
        (20, is_comment("/* Is Multi Line Comment */"), True),
        (21, is_comment("/*"), False),
        (22, is_comment("/* --"), False),
        (23, is_comment("-- /*"), False),
        (24, is_comment("-- Is Single Line Comment"), False),
    ],
)
def test_comments(id, test_input: bool, expected_output: bool):
    assert test_input == expected_output


def test_is_empty_char():
    assert is_empty_char(" ")
    assert is_empty_char("\t")
    assert is_empty_char("\n")
    assert is_empty_char("\r")
    assert not is_empty_char("a")


def test_is_keyword():
    assert is_keyword("SELECT")
    assert not is_keyword("select")


def test_is_number():
    assert is_number("1")
    assert is_number("-1")
    assert is_number("1.1")
    assert is_number("-1.1")
    assert is_number("1.1e2")
    assert is_number("-1.1e2")
    assert is_number("1.1e+2")
    assert is_number("-1.1e+2")
    assert not is_number("a")
    assert not is_number("1.1e2.1")
