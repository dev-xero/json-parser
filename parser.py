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

    # Recursively parse objects
    def parse_object(self):
        self.expect(TokenType.LEFT_BRACE)
        members = self.parse_members()
        self.expect(TokenType.RIGHT_BRACE)

        return members

    # Recursively parse members
    def parse_members(self):
        members = {}
        if self.lookahead() != TokenType.RIGHT_BRACE:
            k, v = self.parse_pair()
            members.update({k: v})
            while self.lookahead() == TokenType.COMMA:
                # consume ,
                self.advance()
                k, v = self.parse_pair()
                members.update({k: v})

        return members

    # Recursively parse pairs
    def parse_pair(self):
        # consume key
        key = self.expect(TokenType.STRING)
        self.expect(TokenType.COLON)

        # consume value
        value = self.parse_value()

        return key, value

    # Recursively parse values
    def parse_value(self):
        ttype = self.lookahead()

        if ttype == TokenType.STRING:
            return self.expect(TokenType.STRING)

        elif ttype == TokenType.NUMBER:
            return int(self.expect(TokenType.NUMBER))

        elif ttype == TokenType.BOOLEAN:
            boolean = self.expect(TokenType.BOOLEAN)
            return True if boolean == 'true' else False

        elif ttype == TokenType.LEFT_BRACE:
            return self.parse_object()

        elif ttype == TokenType.NULL:
            self.expect(TokenType.NULL)
            return None

        else:
            exitWithMsg(f"Unexpected token: {self.tokens[self.pos]}")

    # Helper function: expect a token
    def expect(self, token: Token):
        ttype, value = self.advance()

        if (ttype != token):
            exitWithMsg(
                f"[pos: {self.pos}]: Expected token {token}, but got: {ttype}.")

        return value

    # Helper function: lookahead
    def lookahead(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos].type

        return None

    # Helper function: advance pointer
    def advance(self):
        if self.pos < len(self.tokens):
            token = self.tokens[self.pos]
            self.pos += 1

            return token.type, token.value
