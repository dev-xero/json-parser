from tokens import *


class Lexer:
    """
        This class is responsible for reading the source file and producing valid json tokens.
    """

    # Lexer state
    start, current, line = 0, 0, 1

    # Instantiates a new lexer
    def __init__(self, source: str):
        self.source = source
        self.tokens: [Token] = []
        self.scanning = False

    # Prints source content
    def print_source(self):
        print(self.source)

    # Returns the next character in source
    def look_ahead(self):
        return self.source[self.current+1]

    # Scans the source content and produces json tokens
    def scan(self) -> [Token]:
        self.scanning = True

        while self.current < len(self.source):
            self.start = self.current

            match self.source[self.current]:
                case '{':
                    self.tokens.append(Token(TokenType.LEFT_BRACE, None))

                case '}':
                    self.tokens.append(Token(TokenType.RIGHT_BRACE, None))

                case ':':
                    self.tokens.append(Token(TokenType.COLON, None))

                case ',':
                    self.tokens.append(Token(TokenType.COMMA, None))

                case ' ' | '\n' | '\t':
                    if self.source[self.current] == '\n':
                        self.line += 1

                case '"':
                    # We expect alphanumerics to follow a quote
                    if self.look_ahead().isalnum():
                        while self.current < (len(self.source)-1) and self.look_ahead() != '"':
                            if self.current+2 >= len(self.source):
                                print(
                                    f"[Line {self.line}] Unterminated string literal.")
                                exit(1)

                            if self.current+1 >= len(self.source):
                                break

                            self.current += 1

                        string = self.source[self.start+1:self.current+1]
                        self.tokens.append(Token(TokenType.STRING, string))

                    else:
                        pass

                case _:
                    # Check if this lexeme is a digit, then a potential number
                    current = self.source[self.current]
                    if current.isdigit():
                        while (self.current < len(self.source)) and self.look_ahead().isdigit():
                            if self.current+1 >= len(self.source):
                                break

                            self.current += 1

                        number = self.source[self.start:self.current+1]
                        self.tokens.append(Token(TokenType.NUMBER, number))

                    # Check if this lexeme is a special identifier
                    # null, true, false
                    elif current.isalnum():
                        if self.current + 5 < len(self.source):
                            identifier = self.source[self.current:self.current+4]

                            # If this identifier is either true or null, append appropriately
                            if identifier in ['true', 'null']:
                                if identifier == 'true':
                                    self.tokens.append(
                                        Token(TokenType.BOOLEAN, identifier))
                                else:
                                    self.tokens.append(
                                        Token(TokenType.NULL, identifier))

                            # If scanning the next lexeme will give 'false', append as a boolean
                            elif identifier == 'fals':
                                if self.source[self.current:self.current+5] == 'false':
                                    self.tokens.append(
                                        Token(TokenType.BOOLEAN, 'false'))

                    # Default case, exit on encountering an undefined lexeme
                    else:
                        print(
                            f"[Line {self.line}] Unexpected token '{current}' encountered.")
                        exit(1)

            self.current += 1

        return self.tokens

    # Prints all token type and value
    def print_tokens(self):
        """
            Prints all of the tokens encountered thus far
        """
        for token in self.tokens:
            print("type: {}\nvalue: {}\n".format(token.type, token.value))
