from enum import Enum, auto


class TokenType(Enum):
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COLON = auto()
    COMMA = auto()
    STRING = auto()
    NUMBER = auto()


class Token:
    def __init__(self, token_type: TokenType, value: str | None):
        self.type = token_type
        self.value = value
