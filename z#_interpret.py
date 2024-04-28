from enum import Enum
import re
import sys

'''
Some additional thoughts:
1. Where do I check the grammar?
2. How do I handle multiple lines of commands? (???)
3. Where do I store variables as I'm interpreting code?

'''


class Type(Enum):
    STRING = "STRING"
    IDENTIFIER = "IDENTIFIER"
    OPERATOR = "OPERATOR"
    EOC = "ENDOFCOMMAND"
    EQUALS = "EQUALS"
    NUMBER = "NUMBER"
    COMPARE = "COMPARE"
    BOOLEAN = "BOOLEAN"
    NULL = "NULL"
    FORLOOP = "FORLOOP"
    VARIABLE = "VARIABLE"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
    END = "END"
    FUNCTION = "FUNCTION"
    CHAR = "CHAR"
    INT = "INT"
    DOUBLE = "DOUBLE"
    ENDLINE = "ENDLINE"
    MULTICOM = "MULTICOM"
    SINGLECOM = "SINGLECOM"
    ENDPRINT = "ENDPRINT"
    STARTPRINT = "STARTPRINT"
    ENDQUOTE = "ENDQUOTE"
    STARTQUOTE = "STARTQUOTE"
    IF = "IF"
    ELSE = "ELSE"
    RIGHT_PAREN = "RIGHT_PAREN"
    COMMA = "COMMA"

class Lexer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = []

    def lex(self):
        TOKEN_TYPES = {
            r'\+': Type.OPERATOR,
            r'-': Type.OPERATOR,
            r'\*': Type.OPERATOR,
            r'/': Type.OPERATOR,
            r'=': Type.EQUALS,
            r'>': Type.COMPARE,
            r'<': Type.COMPARE,
            r'\d+': Type.NUMBER,
            r'[a-zA-Z_][a-zA-Z_0-9]*': Type.IDENTIFIER,
            r'<3': Type.ENDLINE,
            r':\((': Type.STARTQUOTE,
            r'\):': Type.ENDQUOTE,
            r'\<>': Type.STARTPRINT,
            r'\<\/\>': Type.ENDPRINT,
            r'\yur\b': Type.SINGLECOM,
            r'\yurrr\b': Type.MULTICOM,
            r'\)': Type.RIGHT_PAREN,
            r',': Type.COMMA,
        }

        KEYWORDS = {
            'valid': Type.COMPARE,
            'sus': Type.COMPARE,
            'nocap': Type.BOOLEAN,
            'cap': Type.BOOLEAN,
            'bruh': Type.NULL,
            'forreal': Type.FORLOOP,
            'jawn': Type.VARIABLE,
            'lowkey': Type.PRIVATE,
            'highkey': Type.PUBLIC,
            'onPeriod': Type.END,
            'toSlay': Type.FUNCTION,
            'worrrd': Type.STRING,
            'rizzler': Type.CHAR,
            'fortnite': Type.INT,
            'dubs': Type.DOUBLE,
            'bussIf': Type.IF,
            'bussElse': Type.ELSE,
        }

        for token in self.input_string.split():
            if token in KEYWORDS:
                self.tokens.append({'Type': KEYWORDS[token], 'value': token})
            else:
                for pattern, token_type in TOKEN_TYPES.items():
                    if re.fullmatch(pattern, token):
                        self.tokens.append({'Type': token_type, 'value': token})
                        break
                else:
                    raise ValueError(f"Unknown token: {token}")
        return self.tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.it = iter(self.tokens)
        self.current_token = next(self.it, None)

    def next_token(self):
        self.current_token = next(self.it, None)

    def parse_program(self):
        statements = []
        while self.current_token:
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
            self.next_token()
        return statements

    def parse_statement(self):
        if (self.current_token['Type'] == Type.INT) or (self.current_token['Type'] == Type.DOUBLE):
            return self.parse_var_declaration()
        elif self.current_token['Type'] == Type.IDENTIFIER:
            return self.parse_function_call()
        elif self.current_token['Type'] == Type.STARTPRINT:
            return self.parse_print_statement()
        elif self.current_token['Type'] == Type.SINGLECOM:
            self.parse_comment()
            return None
        else:
            raise ValueError("Unexpected token")

    def parse_var_declaration(self):
        type_token = self.current_token
        self.next_token()
        if type_token['value'] == 'fortnite':
            type_token['value'] = 'INT'
        if type_token['value'] == 'dubs':
            type_token['value'] = 'DOUBLE'
        identifier_token = self.current_token
        self.next_token()
        if self.current_token['Type'] == Type.EQUALS:
            self.next_token()
            expression = self.parse_expression()
            if not expression:
                raise ValueError("Expected expression after equals")
            return {
                'Type': 'VariableDeclaration',
                'type': type_token['value'],
                'identifier': identifier_token['value'],
                'expression': expression
            }
        else:
            return {
                'Type': 'VariableDeclaration',
                'type': type_token['value'],
                'identifier': identifier_token['value'],
                'expression': None
            }

    def parse_function_call(self):
        identifier_token = self.current_token.next_token()
        left_paren_token = self.current_token
        self.next_token()
        arguments = self.parse_arguments()
        right_paren_token = self.current_token
        self.next_token()
        return {
            'Type': 'FunctionCall',
            'identifier': identifier_token['value'],
            'arguments': arguments
        }

    def parse_print_statement(self):
        print_token = self.current_token
        self.next_token()
        expression = self.parse_expression()
        if not expression:
            raise ValueError("Expected expression after print")
        return {
            'Type': 'PrintStatement',
            'expression': expression
        }

    def parse_comment(self):
        comment_token = self.current_token
        self.next_token()
        while self.current_token and self.current_token['Type'] == Type.SINGLECOM:
            self.next_token()

    def parse_expression(self):
        left = self.parse_term()
        while self.current_token and self.current_token['Type'] in (Type.OPERATOR, Type.EQUALS):
            operator_token = self.current_token
            self.next_token()
            right = self.parse_term()
            left = {
                'Type': 'BinaryOperation',
                'operator': operator_token['value'],
                'left': left,
                'right': right
            }
        return left

    def parse_term(self):
        if self.current_token['Type'] == Type.NUMBER:
            return {
                'Type': 'Literal',
                'value': self.current_token['value']
            }
        elif self.current_token['Type'] == Type.IDENTIFIER:
            return {
                'Type': 'Identifier',
                'value': self.current_token['value']
            }
        elif self.current_token['Type'] == Type.STARTQUOTE:
            return self.parse_string()
        else:
            raise ValueError("Unexpected token")

    def parse_string(self):
        start_quote_token = self.current_token
        self.next_token()
        value = ""
        while self.current_token and self.current_token['Type'] != Type.ENDQUOTE:
            value += self.current_token['value']
            self.next_token()
        end_quote_token = self.current_token
        self.next_token()
        return {
            'Type': 'String',
            'value': value
        }

    def parse_arguments(self):
        arguments = []
        while self.current_token and self.current_token['Type'] != Type.RIGHT_PAREN:
            expression = self.parse_expression()
            if not expression:
                raise ValueError("Expected expression as argument")
            arguments.append(expression)
            if self.current_token and self.current_token['Type'] == Type.COMMA:
                self.next_token()
        return arguments

    def parse(self):
        return self.parse_program()

def pretty_print_ast(ast_list, indent=0):
    """ Recursively prints the AST in a human-readable format with indentation. """
    for ast in ast_list:
        if ast['Type'] == 'Literal':
            print(' ' * indent + f"Literal({ast['value']})")
        elif ast['Type'] == 'BinaryOperation':
            print(' ' * indent + f"BinaryOperation({ast['operator']})")
            print(' ' * indent + '├─ left:')
            pretty_print_ast(ast['left'], indent + 4)
            print(' ' * indent + '└─ right:')
            pretty_print_ast(ast['right'], indent + 4)
        elif ast['Type'] == 'VariableDeclaration':
            print(' ' * indent + f"VariableDeclaration({ast['type']})")
            print(' ' * indent + '├─ identifier:')
            print(' ' * (indent + 4) + f"{ast['identifier']}")
            if 'expression' in ast and ast['expression']:
                print(' ' * indent + '└─ expression:')
                expression_ast = ast['expression']
                if expression_ast['Type'] == 'Literal':
                    print(' ' * (indent + 4) + f"Literal({expression_ast['value']})")
                elif expression_ast['Type'] == 'Identifier':
                    print(' ' * (indent + 4) + f"Identifier({expression_ast['identifier']})")
                else:
                    pretty_print_ast([ast['expression']], indent + 4)


class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_program(self, program):
        for ast in program:
            self.evaluate_ast(ast)

    def evaluate_ast(self, ast):
        """ Recursively evaluates the AST to compute the result of the expression. """
        if ast['Type'] == 'Literal':
            return int(ast['value'])  # Convert the value to an integer and return it

        elif ast['Type'] == 'Identifier':
            return self.variables[ast['value']]

        elif ast['Type'] == 'VariableDeclaration':
            self.variables[ast['identifier']] = self.evaluate_ast(ast['expression']) if ast['expression'] else None
            return self.variables[ast['identifier']]

        elif ast['Type'] == 'BinaryOperation':
            left_val = self.evaluate_ast(ast['left'])  # Recursively evaluate the left child
            right_val = self.evaluate_ast(ast['right'])  # Recursively evaluate the right child

            # Perform the operation based on the operator
            if ast['operator'] == '+':
                return left_val + right_val
            elif ast['operator'] == '-':
                return left_val - right_val
            elif ast['operator'] == '*':
                return left_val * right_val
            elif ast['operator'] == '/':
                if right_val == 0:
                    raise ValueError("Division by zero")  # Handle division by zero
                return left_val / right_val
            else:
                raise ValueError(f"Unsupported operator: {ast['operator']}")


input = ""
debug = True

# Run file without command line
with open("test.genz", "r") as file:
    input = file.read().replace("\n", " ")

################################################################
# Check for Puddle file type, and run on command line
if len(sys.argv) > 1:
    if not sys.argv[1].endswith('.genz'):
        print("Error: The file is not a genZ file.")
        sys.exit()

try:
    with open(sys.argv[1], 'r') as file:
        input = file.read().replace("\n", " ")
except FileNotFoundError:
    print("Error: The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
################################################################

if debug:
    print("\n--------INPUT--------")
    print(input)

tokens = Lexer(input).lex()

if debug:
    print("\n--------TOKENS--------")
    print("")
    for t in tokens:
        print(t)
    print("")

ast = Parser(tokens).parse()

if debug:
    print("\n--------AST--------")
    print(ast)
    pretty_print_ast(ast, 10)

result = Interpreter().evaluate_program(ast)

if debug:
    print("\n--------RESULT--------")
    print(f" The result of your line of code is: {result}\n")
else:
    print(result)