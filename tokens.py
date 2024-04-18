from enum import Enum


class TokenType(Enum):
    LEFT_BRACE = '{'
    RIGHT_BRACE = '}'


class Token:
    def __init__(self, token_type: TokenType, value: str | None):
        self.type = token_type
        self.value = value
