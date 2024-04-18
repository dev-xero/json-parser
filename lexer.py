class Lexer:
    '''
    This class is responsible for reading the source file and producing valid json tokens
    '''
    def __init__(self, source: str):
        self.source = source

    def print_source(self):
        print(self.source)
