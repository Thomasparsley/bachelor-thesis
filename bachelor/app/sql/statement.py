from .enum import StatementVariant
from .token import (
    BinaryExpressionToken,
    ExpressionToken,
    KeywordToken,
    MapToken,
    Token,
    IdentifierToken,
)


class Statement:
    def __init__(self, variant: StatementVariant):
        self.variant = variant


class SelectStatement(Statement):
    select: KeywordToken
    result: list[Token]
    from_: IdentifierToken | MapToken
    where: list[BinaryExpressionToken] | None
    order: ExpressionToken | None

    def __init__(self):
        super().__init__(StatementVariant.SELECT)


class UpdateStatement(Statement):
    def __init__(self):
        super().__init__(StatementVariant.UPDATE)
