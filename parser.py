from tokens import *


class Parser:
    def __init__(self, tokens):
        self.tokens: [Token] = tokens
        self.pos: int = 0

    def parse(self) -> dict:
        return self.parse_value()

    def parse_value(self):
        token, value = self.advance()
        if token == TokenType.NUMBER:
            return {"Number": value}

    # Helper function
    def advance(self):
        if self.pos < len(self.tokens):
            self.pos += 1;
            return self.tokens[self.pos].type, self.tokens[self.pos].value
