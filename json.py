from lexer import Lexer


def read_file(path: str) -> str:
    """
        Reads the contents of the file specified by the path.
        - path: string file path
    """
    output = ''

    try:
        with open(path) as file:
            output = file.read()

    except FileNotFoundError:
        print("Failed to read json file.")
        exit(1)

    return output.strip()


def main():
    """
        Main program entry point.
    """
    path = input("> JSON File: ")

    if path == '':
        print("No file specified.")
        exit(1)

    file = read_file(path)

    if file == '':
        print("Failed to read json file.")
        exit(1)

    # Generates tokens from the source file
    lexer = Lexer(file)

    lexer.scan()
    lexer.print_tokens()


if __name__ == "__main__":
    main()
