from lexer import Lexer
from pathlib import Path

def read_file(path: str):
    '''
        Reads the contents of the file specified by the path.
        - path: string file path
    '''
    output = ''

    try:
        with open(path) as file:
            output = file.read()
    except:
        print("Failed to read json file.")
        exit(1)

    return output


def main():
    '''Main program entry point.'''
    path = input("> JSON File: ")

    if path == '':
        print("No file specified.")
        exit(1)

    file = read_file(path)
    
    if file == '':
        print("Failed to read json file.")
        exit(1)

    lexer = Lexer(file)
    lexer.print_source()


if __name__ == "__main__":
    main()
