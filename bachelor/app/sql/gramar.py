from pyparsing import (
    Word,
    delimited_list,
    Optional,
    Group,
    alphas,
    alphanums,
    Forward,
    one_of,
    quoted_string,
    infix_notation,
    OpAssoc,
    rest_of_line,
    ParserElement,
    pyparsing_common as ppc,
)

from .tokens import (
    ASC,
    DESC,
    DISTINCT,
    SELECT,
    FROM,
    WHERE,
    IN,
    IS,
    NOT,
    NOT_NULL,
    NULL,
    AND,
    OR,
    LIKE,
    BETWEEN,
    ORDER_BY,
    WILDCARD,
)

#
# Forwarded statements
#
statement_select = Forward()
statement_update = Forward()
statement_delete = Forward()

identifier = Word(alphas, alphanums + "_$").set_name("identifier")

column_name = delimited_list(identifier, ".", combine=True)
column_name.set_name("column_name")
column_name.add_parse_action(  # type: ignore
    ppc.upcaseTokens,
)

column_name_list = Group(delimited_list(column_name).set_name("column_name_list"))

table_name = delimited_list(identifier, ".", combine=True)
table_name.set_name("table_name")
table_name.add_parse_action(  # type: ignore
    ppc.upcaseTokens,
)

table_name_list = Group(delimited_list(table_name).set_name("table_name_list"))

binary_op = one_of("= != < > >= <= <> eq ne lt le gt ge", caseless=True)
binary_op.set_name("binary_op")

real_number = ppc.real()
real_number.set_name("real_number")

integer_number = ppc.signed_integer()
integer_number.set_name("integer_number")

# TODO: add support for alg expressions
value = integer_number | integer_number | quoted_string | column_name
value.setName("value")

condition_where = Group(
    (column_name + binary_op + value)
    | (
        column_name
        + IN
        + Group("(" + delimited_list(value).set_name("in_values_list") + ")")
    )
    | (column_name + IN + Group("(" + statement_select + ")"))  # type: ignore
    | (column_name + IS + (NULL | NOT_NULL))
    | (column_name + LIKE + quoted_string)
    | (column_name + BETWEEN + value + AND + value)
)

expression_where = infix_notation(
    condition_where,
    [
        (NOT, 1, OpAssoc.RIGHT),
        (AND, 2, OpAssoc.LEFT),
        (OR, 2, OpAssoc.LEFT),
    ],
)
expression_where.set_name("where_expression")

block_select = Group(SELECT + DISTINCT | SELECT) + (WILDCARD | column_name_list)(
    "columns"
)
block_from = FROM + table_name_list("tables")
block_where = Optional(Group(WHERE + expression_where), "")("where")
block_order_by = Optional(Group(ORDER_BY + column_name_list + (ASC | DESC)), "")(
    "order_by"
)

statement_select: ParserElement
statement_select <<= block_select + block_from + block_where + block_order_by

comment = "--" + rest_of_line
