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
    OPERATOR = "OPERATOR"
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
    STRING = "STRING"
    CHAR = "CHAR"
    INT = "INT"
    DOUBLE = "DOUBLE"
    # PRINT + RETURN
    ENDLINE = "ENDLINE"
    # QUOTE
    # SINGLE LINE COMMENT
    # MULTI LINE COMMENT
    IF = "IF"
    ELSE = "ELSE"


class Lexer:
    def __init__(self, i):
        self.i = i.split()
        self.out = []

    def lex(self):
        # patterns to check
        z_add = r'\+'
        z_sub = r'\-'
        z_multi = r'\*'
        z_div = r'\/'

        z_valid = r'\valid'
        z_sus = r'\sus'
        z_great = r'\>'
        z_less = r'\<'

        z_equal = r'\='

        z_digits = r'^\d+$'

        z_nocap = r'\nocap\b'
        z_cap = r'\cap\b'
        z_bruh = r'\bruh\b'
        z_forreal = r'\forreal\b'
        z_jawn = r'\jawn\b'
        z_lowkey = r'\lowkey\b'
        z_highkey = r'\highkey\b'
        z_onPeriod = r'\onPeriod\b'
        z_toSlay = r'\toSlay\b'
        z_worrrd = r'\worrrd\b'
        z_rizzler = r'\rizzler\b'
        z_fortnite = r'\fortnite\b'
        z_dubs = r'\dubs\b'
        z_startPrint = r'<>'
        z_endPrint = r'<\/\>'
        z_endLine = r'<3'
        z_startQuote = r':\('
        z_endQuote = r'\):'
        z_singleCom = r'\yur\b'
        z_multiCom = r'\yurrr\b'
        z_if = r'\bussIf\b'
        z_else = r'\bussElse\b'



        for token in self.i:
            # OPERATOR
            if re.fullmatch(z_add, token):
                self.out.append({"Type": Type.OPERATOR, "value": token})
            elif re.fullmatch(z_sub, token):
                self.out.append({"Type": Type.OPERATOR, "value": token})
            elif re.fullmatch(z_multi, token):
                self.out.append({"Type": Type.OPERATOR, "value": token})
            elif re.fullmatch(z_div, token):
                self.out.append({"Type": Type.OPERATOR, "value": token})
            # COMPARE
            elif token == "valid":  # Check for the word "valid"
                self.out.append({"Type": Type.COMPARE, "value": token})  # Create a token for it
            elif token == "sus":  # Check for the word "sus"
                self.out.append({"Type": Type.COMPARE, "value": token})  # Create a token for it
            elif re.fullmatch(z_great, token):
                self.out.append({"Type": Type.COMPARE, "value": token})
            elif re.fullmatch(z_less, token):
                self.out.append({"Type": Type.COMPARE, "value": token})
            elif re.fullmatch(z_equal, token):
                self.out.append({"Type": Type.COMPARE, "value": token})
            # NUMBER
            elif re.fullmatch(z_digits, token):
                self.out.append({"Type": Type.NUMBER, "value": token})
            # BOOLEAN
            elif token == "nocap":  # Check for the word "nocap"
                self.out.append({"Type": Type.BOOLEAN, "value": token})  # Create a token for it
            elif token == "cap":  # Check for the word "cap"
                self.out.append({"Type": Type.BOOLEAN, "value": token})  # Create a token for it
            # NULL
            elif token == "bruh":  # Check for the word "bruh"
                self.out.append({"Type": Type.NULL, "value": token})  # Create a token for it
            # FORLOOP
            elif token == "forreal":  # Check for the word "forreal"
                self.out.append({"Type": Type.FORLOOP, "value": token})  # Create a token for it
            # VARIABLE
            elif token == "jawn":  # Check for the word "jawn"
                self.out.append({"Type": Type.VARIABLE, "value": token})  # Create a token for it
            # PRIVATE
            elif token == "lowkey":  # Check for the word "lowkey"
                self.out.append({"Type": Type.PRIVATE, "value": token})  # Create a token for it
            # PUBLIC
            elif token == "highkey":  # Check for the word "highkey"
                self.out.append({"Type": Type.PUBLIC, "value": token})  # Create a token for it
            # END
            elif token == "onPeriod":  # Check for the word "onPeriod"
                self.out.append({"Type": Type.END, "value": token})  # Create a token for it
            # FUNCTION
            elif token == "toSlay":  # Check for the word "toSlay"
                self.out.append({"Type": Type.FUNCTION, "value": token})  # Create a token for it
            # STRING
            elif token == "worrrd":  # Check for the word "worrrd"
                self.out.append({"Type": Type.STRING, "value": token})  # Create a token for it
            # CHAR
            elif token == "rizzler":  # Check for the word "rizzler"
                self.out.append({"Type": Type.CHAR, "value": token})  # Create a token for it
            # INT
            elif token == "fortnite":  # Check for the word "fortnite"
                self.out.append({"Type": Type.INT, "value": token})  # Create a token for it
            # DOUBLE
            elif token == "dubs":  # Check for the word "dubs"
                self.out.append({"Type": Type.DOUBLE, "value": token})  # Create a token for it
            # PRINT + RETURN
            # ENDLINE
            elif re.fullmatch(z_endLine, token):
                self.out.append({"Type": Type.ENDLINE, "value": token})
            # QUOTE
            # SINGLE LINE COMMENT
            # MULTI LINE COMMENT
            # IF
            elif token == "bussIf":  # Check for the word "bussIf"
                self.out.append({"Type": Type.IF, "value": token})  # Create a token for it
            # ELSE
            elif token == "bussEls":  # Check for the word "bussEls"
                self.out.append({"Type": Type.ELSE, "value": token})  # Create a token for it

            # Example for token keyword search:
            # This is how You check for full words - start with going through and doing all these
            elif token == "nocap":  # Check for the word "nocap"
                self.out.append({"Type": Type.BOOLEAN, "value": token})  # Create a token for it

        return self.out


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.it = iter(self.tokens)
        self.current_token = next(self.it, None)

    def next_token(self):
        """ Advances to the next token, if available. """
        self.current_token = next(self.it, None)

    def parse(self):
        '''
        BEFORE you build the AST, check that the command is
        a valid grammar.
        '''

        """ Parses the tokens into an AST based on simple arithmetic rules. """
        if not self.current_token:
            return None  # Early exit if there are no tokens

        # Start with the first literal
        left = {'Type': 'Literal', 'value': self.current_token['value']}
        self.next_token()

        # Process as long as there are tokens and the current token is an operator
        while self.current_token and self.current_token['Type'] == Type.OPERATOR:
            operator = self.current_token['value']
            self.next_token()
            if not self.current_token or self.current_token['Type'] != Type.NUMBER:
                raise ValueError("Expected a number after operator")

            right = {'Type': 'Literal', 'value': self.current_token['value']}
            left = {
                'Type': 'BinaryOperation',
                'operator': operator,
                'left': left,
                'right': right
            }
            self.next_token()

        return left


def pretty_print_ast(ast, indent=0):
    """ Recursively prints the AST in a human-readable format with indentation. """
    if ast['Type'] == 'Literal':
        print(' ' * indent + f"Literal({ast['value']})")
    elif ast['Type'] == 'BinaryOperation':
        print(' ' * indent + f"BinaryOperation({ast['operator']})")
        print(' ' * indent + '├─ left:')
        pretty_print_ast(ast['left'], indent + 4)
        print(' ' * indent + '└─ right:')
        pretty_print_ast(ast['right'], indent + 4)


class Interpreter:
    def __init__(self):
        pass

    def evaluate_ast(self, ast):
        """ Recursively evaluates the AST to compute the result of the expression. """
        if ast['Type'] == 'Literal':
            return int(ast['value'])  # Convert the value to an integer and return it

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
    pretty_print_ast(ast)

result = Interpreter().evaluate_ast(ast)

if debug:
    print("\n--------RESULT--------")
    print(f" The result of your line of code is: {result}\n")
else:
    print(result)