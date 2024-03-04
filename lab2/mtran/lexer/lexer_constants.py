syntax_types = {
    "int": "DATA_TYPE",
    "float": "DATA_TYPE",
    "double": "DATA_TYPE",
    "char": "DATA_TYPE",
    "void": "DATA_TYPE",
    "string": "DATA_TYPE",
    "identifier": "VARIABLE",
    "const": "CONSTANT_VALUE",
    "string_value": "STRING_CONST",
    'comment': 'COMMENT',
    "if": "BUILD_IN",
    "rand": "BUILD_IN",
    "else": "BUILD_IN",
    "while": "BUILD_IN",
    "for": "BUILD_IN",
    "break": "BUILD_IN",
    "continue": "BUILD_IN",
    "return": "BUILD_IN",
    "sizeof": "BUILD_IN",
    "cout": "BUILD_IN",
    "endl": "BUILD_IN",
    "[": "LEFT_SQUARE_BRACKET",
    "]": "RIGHT_SQUARE_BRACKET",
    "{": "LEFT_CURLY_BRACKET",
    "}": "RIGHT_CURLY_BRACKET",
    "(": "LEFT_ROUND_BRACKET",
    ")": "RIGHT_ROUND_BRACKET",
    ",": "COMMA",
    ";": "SEMICOLON",
    "+": "ARITHMETIC_OPERATION",
    "-": "ARITHMETIC_OPERATION",
    "++": "ARITHMETIC_OPERATION",
    "--": "ARITHMETIC_OPERATION",
    "*": "ARITHMETIC_OPERATION",
    "/": "ARITHMETIC_OPERATION",
    "%": "ARITHMETIC_OPERATION",
    "=": "ARITHMETIC_OPERATION",
    "+=": "ARITHMETIC_OPERATION",
    "*=": "ARITHMETIC_OPERATION",
    "/=": "ARITHMETIC_OPERATION",
    "-=": "ARITHMETIC_OPERATION",
    "<": "COMPARISON_SIGN",
    ">": "COMPARISON_SIGN",
    "<=": "COMPARISON_SIGN",
    ">=": "COMPARISON_SIGN",
    "==": "COMPARISON_SIGN",
    "!=": "COMPARISON_SIGN",
    "<<": "OVERRIDE_OPERATION",
    ">>": "OVERRIDE_OPERATION",
    "function": "FUNCTION"
}
nodes = (
    "Block_node",
    "Else_node",
    "If_node",
    "While_node",
    "For_node",
    "Expression_node",
    "Func_declaration_node",
    "Variable_node",
    "Func_node",
    "Compare_node",
    "Assign_node",
    "Build_in_node"
)
tags = (
    ('DATA_TYPE'),
    ('VARIABLE'),
    ('CONSTANT_VALUE'),
    ('STRING_CONST'),
    ('COMMENT'),
    ('BUILD_IN'),
    ('LEFT_SQUARE_BRACKET', 'RIGHT_SQUARE_BRACKET', 'LEFT_CURLY_BRACKET', 'RIGHT_CURLY_BRACKET', 'LEFT_ROUND_BRACKET',
     'RIGHT_ROUND_BRACKET'),
    ('COMMA', 'SEMICOLON'),
    ('ARITHMETIC_OPERATION'),
    ('COMPARISON_SIGN'),
    ('OVERRIDE_OPERATION'),
    ('FUNCTION')
)
regex_map = {
    'function': r'(\w+)\s+(\w+)(?=\()([^)]*?)\s*',
    'int': r'int\b',
    'float': r'float\b',
    'double': r'double\b',
    'char': r'char\b',
    'bool': r'bool\b',
    'string': r'string\b',
    'if': r'if\b',
    'else': r'else\b',
    'for': r'for\b',
    'while': r'while\b',
    'do': r'do\b',
    'break': r'break\b',
    'continue': r'continue\b',
    'return': r'return\b',
    'void': r'void\b',
    'sizeof': r'sizeof\b',
    'cin': r'cin\b',
    'rand': r'rand\b',
    'cout': r'cout\b',
    'endl': r'endl\b',
    'identifier': r'[a-zA-Z_]\w*',
    'const': r'\d+(\.\d+)*',
    'string_value': r'\".+?\"',
    'operator': r'[+\-*/%<>&|^=!]+|<<|>>',
    'semicolon': r';',
    'comma': r',',
    'comment': r'//.*?$|/\*.*?\*/',
    'whitespace': r'[\t|\n|\s|\r]+',
    'left_round_bracket': r'\(',
    'right_round_bracket': r'\)',
    'left_square_bracket': r'\[',
    'right_square_bracket': r'\]',
    'left_curly_bracket': r'\{',
    'right_curly_bracket': r'\}'
}
c_plus_plus_libraries = [
    "#include<iostream>",
    "#include<algorithm>",
    "#include<vector>",
    "#include<map>",
    "#include<set>",
    "#include<queue>",
    "#include<stack>",
    "#include<cmath>",
    "#include<cstring>",
    "#include<fstream>",
    "#include<sstream>",
    "#include<cstdlib>",
    "#include<ctime>",
    "#include<bitset>",
    "#include<unordered_map>"
]