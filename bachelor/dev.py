# from app.sql.parser.parser import parser
#
# parser("SELECT * FROM datatable_1; SELECT one FROM datatable_2")

from typing import Any

# from pyparsing import Word, alphas
#
#
# greet = Word(alphas) + "," + Word(alphas) + "!"
# hello = "Hello, World!"
# a = greet.parseString(hello)
#
# print(hello, "->", greet.parseString(hello))

# from typing import Any
#
import sqlparse  # type: ignore

#
# from app.consts import SQL_MACROS
#
#
# query = """
# SELECT *
# FROM datatable
# where years>'1993'
# """
#
# query = sqlparse.format(  # type: ignore
#     query,
#     reindent=True,
#     keyword_case="upper",
#     use_space_around_operators=True,
# )
#
# a = """
# --begin-sql
# SELECT dataset_1_select
# FROM dataset_1
# SYMDIFF
# SELECT dataset_2_select
# FROM dataset_2
#
# /**/
#
# SELECT *
# FROM (
#     SELECT {dataset_1_select}
#     FROM dataset_1
#     UNION
#     SELECT {dataset_2_select}
#     FROM dataset_2
# ) AS symdiff_{random}
# EXCEPT
# SELECT *
# FROM (
#     SELECT {dataset_1_select}
#     FROM dataset_1
#     INTERSECT
#     SELECT {dataset_2_select}
#     FROM dataset_2
# ) AS symdiff_{random}
# --end-sql
# """
#
