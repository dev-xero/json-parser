from tokens import *


class Lexer:
    """
        This class is responsible for reading the source file and producing valid json tokens.
    """

    def __init__(self, source: str):
        self.source = source
        self.tokens: [Token] = []

    def print_source(self):
        print(self.source)

    def scan(self) -> [Token]:
        for lexeme in self.source:
            match lexeme:
                case '{':
                    self.tokens.append(Token(TokenType.LEFT_BRACE, None))

                case '}':
                    self.tokens.append(Token(TokenType.RIGHT_BRACE, None))

                case _:
                    print("Invalid character {} encountered.".format(lexeme))
                    exit(1)

        return self.tokens

    def print_tokens(self):
        for token in self.tokens:
            print(TokenType(token.type))
