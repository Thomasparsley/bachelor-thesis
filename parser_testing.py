from bachelor.app.sql import parse

a = parse(
    """
    SELECT dataset_1_select
    FROM dataset_1

    SYMDIFF

    SELECT dataset_2_select
    FROM dataset_2

    SYMDIFF

    SELECT dataset_3_select
    FROM dataset_3
    """
)

print(a)
