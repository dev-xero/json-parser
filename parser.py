from tokens import *
from lib import exitWithMsg


class Parser:
    """
        This class is responsible for recursively parsing tokens to produce a dictionary
    """

    # Instantiates a new parser
    def __init__(self, tokens):
        self.tokens: [Token] = tokens
        self.pos: int = 0

    # Parse tokens
    def parse(self) -> dict:
        return self.parse_object()

    # Recursively parses objects
    def parse_object(self):
        self.expect(TokenType.LEFT_BRACE)
        members = self.parse_members()
        self.expect(TokenType.RIGHT_BRACE)

        return {"Object": members}

    # Recursively parses members
    def parse_members(self):
        return ''

    # Helper function: expect a token
    def expect(self, token: Token):
        ttype, value = self.advance()

        if (ttype != token):
            exitWithMsg("Expected token {token}, but got: {token_type}.")

        return value

    # Helper function: advance pointer
    def advance(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1

            return token.type, token.value
