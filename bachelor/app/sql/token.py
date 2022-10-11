from .region import Region
from .enum import (
    Direction,
    Keyword,
    TokenFormat,
    TokenOperation,
    TokenType,
    TokenVariant,
)


class Token:
    type: TokenType
    region: Region
    alias: str | None = None


class KeywordToken(Token):
    type = TokenType.KEYWORD
    keyword: Keyword


class IdentifierToken(Token):
    variant: TokenVariant
    name: str


class FunctionToken(Token):
    value: IdentifierToken
    args: None


class ExpressionToken(Token):
    type = TokenType.EXPRESSION
    format: TokenFormat
    variant: TokenVariant


class OrderExpressionToken(ExpressionToken):
    variant = TokenVariant.ORDER
    expression: IdentifierToken
    direction: Direction


class BinaryExpressionToken(ExpressionToken):
    format = TokenFormat.BINARY
    operation: TokenOperation
    left: Token
    right: Token


class MapToken(Token):
    pass
