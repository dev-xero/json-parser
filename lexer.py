from tokens import *


class Lexer:
    """
        This class is responsible for reading the source file and producing valid json tokens.
    """

    start = 0
    current = 0

    def __init__(self, source: str):
        self.source = source
        self.tokens: [Token] = []

    def print_source(self):
        print(self.source)

    def is_end(self):
        return self.current >= len(self.source)

    def look_ahead(self):
        return self.source[self.current+1]

    def scan(self) -> [Token]:
        for i in range(len(self.source)):
            self.current = i
            self.start = self.current
            match self.source[i]:
                case '{':
                    self.tokens.append(Token(TokenType.LEFT_BRACE, None))

                case '}':
                    self.tokens.append(Token(TokenType.RIGHT_BRACE, None))

                case ':':
                    self.tokens.append(Token(TokenType.COLON, None))

                case ',':
                    self.tokens.append(Token(TokenType.COMMA, None))

                case '"':
                    if self.look_ahead().isalnum():
                        while not self.is_end() and self.current < (len(self.source)-1) and self.look_ahead() != '"':
                            if self.current+2 >= len(self.source):
                                print("Unterminated string literal.")
                                exit(1)

                            i += 1
                            if self.current+1 >= len(self.source):
                                break
                            self.current += 1

                        string = self.source[self.start+1:self.current+1]
                        self.tokens.append(Token(TokenType.STRING, string))

                    else:
                        pass

                case _:
                    pass

        return self.tokens

    def print_tokens(self):
        for token in self.tokens:
            print("type: {}\nvalue: {}\n".format(token.type, token.value))
