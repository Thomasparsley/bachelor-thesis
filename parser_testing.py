from bachelor.app.sql import parse


print(
    parse(
        "SELECT * FROM Products WHERE Price BETWEEN 50 AND 60 OR asd is null ORDER BY column1, column2 DESC;"
    )
)
