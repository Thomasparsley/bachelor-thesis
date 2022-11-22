from pyparsing import CaselessKeyword


KEYWORDS = "*, select, distinct, from, where, and, or, in, is, not, null, like, between, order by, asc, desc, union, symdiff".upper().split(
    ", "
)

(
    WILDCARD,
    SELECT,
    DISTINCT,
    FROM,
    WHERE,
    AND,
    OR,
    IN,
    IS,
    NOT,
    NULL,
    LIKE,
    BETWEEN,
    ORDER_BY,
    ASC,
    DESC,
    UNION,
    SYMDIFF,
) = map(CaselessKeyword, KEYWORDS)
NOT_NULL = NOT + NULL
