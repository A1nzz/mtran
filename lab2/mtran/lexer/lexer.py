import re
from tabulate import tabulate
from lexer.lexer_constants import regex_map, syntax_types
import pandas as pd


class CustomToken:
    def __init__(self, value, token_type, line, column):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return f"token with value: {self.value}, type: {self.token_type}, line {self.line}, column {self.column}"



class Lexer:
    def __init__(self):
        self.func_list = []
        self.tokens = []
        self.errors = []
        self.line_num = 1
        self.col_num = 1
        self.cur_func = ""

    def get_tokens(self, code):
        self.tokens = []
        self.errors = []
        self.line_num = 1
        self.col_num = 1
        self.cur_func = ""
        i = 0
        while i < len(code):
            match = None
            for key, value in regex_map.items():
                tag, pattern = key, value
                regex = re.compile(pattern)
                match = regex.match(code[i:])
                #print(key, value)
                if match:
                    text = match.group(0)
                    if tag == "function":
                        text = text.split()
                        if len(self.tokens) != 0:
                            self.func_list.append((self.cur_func, self.tokens))
                            self.tokens = []
                        if not text[0] in syntax_types:
                            print(f"\033[31m[ERROR] lex error: unknown '{text[0]}' at line {self.line_num}, column {self.col_num}\033[0m")
                            exit()
                        token = CustomToken(text[0], syntax_types[text[0]], self.line_num, self.col_num)
                        self.tokens.append(token)
                        self.col_num += len(text[0])
                        token = CustomToken(text[1], syntax_types[tag], self.line_num, self.col_num)
                        self.tokens.append(token)
                        self.col_num += len(text[1])
                        self.cur_func = text[1]
                    elif tag == "whitespace":
                        if '\n' in text:
                            self.line_num += 1
                            self.col_num = 1
                    elif tag == "operator":
                        if len(text) > 2 or self.tokens[-1].token_type == "ARITHMETIC_OPERATION" or text not in syntax_types:
                            print(
                                f"\033[31m[ERROR] unexpected operator '{text}' at line {self.line_num}, column {self.col_num}\033[0m")
                            exit()
                            self.col_num += len(text)
                        else:
                            token = CustomToken(text, syntax_types[text], self.line_num, self.col_num)
                            self.tokens.append(token)
                            self.col_num += len(text)
                    elif tag == "string_value":
                        token = CustomToken(text, syntax_types[tag], self.line_num, self.col_num)
                        self.tokens.append(token)
                        self.col_num += len(text)
                    elif tag == "identifier":
                        token = CustomToken(text, syntax_types[tag], self.line_num, self.col_num)
                        for item in self.func_list:
                            if item[0] == text:
                                token.token_type = "FUNCTION"
                        self.tokens.append(token)
                        self.col_num += len(text)
                    elif tag == "const":
                        if text.count('.') > 1:
                            print(
                                f"\033[31m[ERROR] unexpected value '{text}' at line {self.line_num}, column {self.col_num}\033[0m")
                            exit()
                            self.col_num += len(text)
                        else:
                            token = CustomToken(text, syntax_types[tag], self.line_num, self.col_num)
                            self.tokens.append(token)
                            self.col_num += len(text)
                    else:
                        token = CustomToken(text, syntax_types[text], self.line_num, self.col_num)
                        self.tokens.append(token)
                        self.col_num += len(text)
                    break
            if not match and not code[i] in [':', '#']:
                print(f"\033[31m[ERROR] unexpected character '{code[i]}' at line {self.line_num}, column {self.col_num}\033[0m")
                exit()
                #self.col_num += 1
                #i += 1
            else:
                if code[i] in [':', '#']:
                    i+=1
                else:
                    i += len(match.group(0))

        
        self.func_list.append((self.cur_func, self.tokens))
        const_map = dict()
        var_map = dict()
        build_map = dict()
        square_map = dict()
        arithmetic_map = dict()
        function_map = dict()
        cont_list = ['vector','map','set','unordered_map', 'list', 'deque', 'queue', 'unordered_set']
        prev = None
        s_data = []
        cur_deep = 0
        for token in self.tokens:
            if token.token_type == 'VARIABLE':
                if not token.value in var_map:
                    if prev == None and not token.value in cont_list:
                        print(f"\033[31m[ERROR] lex error: unknown {token.value} at line {token.line}, column {token.column}\033[0m")
                        exit()
                    elif prev.token_type != 'DATA_TYPE' and not token.value in cont_list and token.value != 'std':
                        if prev.value != '>':
                            print(f"\033[31m[ERROR] lex error: unknown {token.value} at line {token.line}, column {token.column}\033[0m")
                            exit()
                    var_map[token.value] = [f"id_{len(var_map)}", prev.value]
                    
            
            if token.token_type == 'CONSTANT_VALUE':
                const_map[token.value] = [token.line, token.column]
            print(token.value, ' ---- ', token.token_type)

            if token.token_type == 'BUILD_IN':
                build_map[token.value] = [token.line, token.column]

            if token.token_type in ['RIGHT_CURLY_BRACKET', 'LEFT_ROUND_BRACKET', 'RIGHT_ROUND_BRACKET', 'LEFT_CURLY_BRACKET']:
                if token.value in ['{', '(']:
                    cur_deep += 1
                else:
                    cur_deep -= 1
                
                if cur_deep < 0:
                    print(f"\033[31[ERROR] unexpected end of file at line {token.line}, {token.column}\033[0m")
                    exit()
                square_map[token.value] = [token.line, token.column, token.token_type]
                s_data.append({'val': token.value, 'row': token.line, 'column': token.column, 'type': token.token_type})

            if token.token_type == 'ARITHMETIC_OPERATION':
                arithmetic_map[token.value] = [token.line, token.column]

            if token.token_type == 'FUNCTION':
                function_map[token.value] = [token.line, token.column]

            prev = token


        if cur_deep != 0:
            print(f"\033[31[ERROR] unexpected end of file at line {self.line_num}, {self.col_num}\033[0m")
            exit()
        df = pd.DataFrame.from_dict(var_map, orient='index', columns=['id', 'data_type'])
        df.reset_index(inplace=True)
        df.columns = ['variable', 'id', 'data_type']
        print('vars')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


        
        df = pd.DataFrame(const_map.items(), columns=['Value', 'Position'])
        print('constants')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        df = pd.DataFrame(build_map.items(), columns=['Value', 'Position'])
        print('builds')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

        df = pd.DataFrame(s_data)
        print('square')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


        df = pd.DataFrame(arithmetic_map.items(), columns=['Value', 'Position'])
        print('arithmetic operators')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        
        df = pd.DataFrame(function_map.items(), columns=['Value', 'Position'])
        print('functions')
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))
        
        pattern = r'#include\s*<([^\s>]*)>'
        libraries = re.findall(pattern, code)
        print("Подключенные библиотеки:")
        for library in libraries:
            print(library)
        
        pattern = r'std::\s*(vector|map|set|unordered_map|list|queue|deque)\s*<\s*(.*?)\s*>\s*(\w+)'

        matches = re.findall(pattern, code)
        print("Найденные контейнеры:")
        for match in matches:
            container_type = match[0]
            container_data_type = match[1]
            container_name = match[2]
            print(f"Тип контейнера: {container_type}, Тип данных: {container_data_type}, Имя контейнера: {container_name}")

        with open('tokenize.txt', "w") as file:
            for token in self.tokens:
                if token.value in var_map:
                    file.write(var_map[token.value][0])
                    file.write(' ')
                else:
                    file.write(token.value)
                    file.write(' ') 
        return self.func_list, self.errors
