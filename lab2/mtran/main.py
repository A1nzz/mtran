
from lexer.lexer import Lexer

if __name__ == "__main__":
    cpp_file = "test.cpp"
    with open(cpp_file, "r") as file:
        code = (file.read())
    custom_lexer = Lexer()
    tokens, errors = custom_lexer.get_tokens(code)
    print('\033[32mOK\033[0m')

    
