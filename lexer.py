from tokens import *


class Lexer:
    """
        This class is responsible for reading the source file and producing valid json tokens.
    """

    # Lexer state
    start, current, line = 0, 0, 0

    # Instantiates a new lexer
    def __init__(self, source: str):
        self.source = source
        self.tokens: [Token] = []

    # Prints source content
    def print_source(self):
        print(self.source)

    # Returns the next character in source
    def look_ahead(self):
        return self.source[self.current+1]

    # Scans the source content and produces json tokens
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

                case ' ' | '\n' | '\t':
                    if self.source[i] == '\n':
                        self.line += 1

                case '"':
                    # We expect alphanumerics to follow a quote
                    if self.look_ahead().isalnum():
                        while self.current < (len(self.source)-1) and self.look_ahead() != '"':
                            if self.current+2 >= len(self.source):
                                print(
                                    f"[Line {self.line}] Unterminated string literal.")
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
                    # Default case, exit on encountering an undefined lexeme
                    current = self.source[i]
                    if not current.isalnum():
                        print(
                            f"[Line {self.line}] Unexpected token '{current}' encountered.")
                        exit(1)

        return self.tokens

    # Prints all token type and value
    def print_tokens(self):
        for token in self.tokens:
            print("type: {}\nvalue: {}\n".format(token.type, token.value))
