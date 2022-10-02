from typing import Any

import sqlparse  # type: ignore

from app.consts import SQL_MACROS


query = """
SELECT *
FROM datatable
where years>'1993'
"""

query = sqlparse.format(  # type: ignore
    query,
    reindent=True,
    keyword_case="upper",
    use_space_around_operators=True,
)

a = """
--begin-sql
SELECT dataset_1_select
FROM dataset_1
SYMDIFF
SELECT dataset_2_select
FROM dataset_2

/**/

SELECT *
FROM (
    SELECT {dataset_1_select}
    FROM dataset_1
    UNION
    SELECT {dataset_2_select}
    FROM dataset_2
) AS symdiff_{random}
EXCEPT
SELECT *
FROM (
    SELECT {dataset_1_select}
    FROM dataset_1
    INTERSECT
    SELECT {dataset_2_select}
    FROM dataset_2
) AS symdiff_{random}
--end-sql
"""

response = sqlparse.parse(
    """
SELECT dataset_1_select
FROM dataset_1
SYMDIFF
SELECT dataset_2_select
FROM dataset_2
"""
)

parsed = response[0]

for _token in response[0].tokens:  # type: ignore
    token: Any = _token

    print(bytes(str(token), "utf-8"))
    if str(token) in SQL_MACROS:
        print(token)


#
# Makro pro relační dělení
