# Z# Language
<img width="216" alt="Screenshot 2024-04-25 at 2 36 39 PM" src="https://github.com/chris-eelman/programming-language-project/assets/78044530/25ad94a6-d5d5-41b7-ab9c-6b879db2f3ee">

Written in: Python

Group members: Chris Eelman, Caleb Rudloff, Laina Nguyen, Jake Gabriels

## Language Overview
Z# is a unique programming language designed with the GenZ in mind. It’s based on Python, a popular high-level
programming language known for its readability and simplicity. However, Z# takes a different approach by 
incorporating modern slang and cultural references into its syntax, making it a fun and engaging way to 
learn programming.

## Syntax

* True: `nocap`
* False: `cap`
* Null: `bruh`
* For loop: `forreal`
* Variable: `jawn`
* Private: `lowkey`
* Public: `highkey`
* End: `onPeriod`
* Function: `toSlay`
* String: `worrrd`
* Char: `rizzler`
* Int: `fortnite`
* Double: `dubs`
* Print/return: `<>` "print statement here" + var `</>`
* To end a line: `<3`
* ‘==’  `valid`
* != `sus`
* Quote: `:(` quote `):`
* Single-line comment: `yur`
* Multi-line comment: `yurrr yurrr`
* If: `bussIf`
* Else: `bussEls`

## Features

* Add random slang to the end of every print statement: `slang()`
* Uno reverse: `unoReverse()` - flip sign (+ or -)
* Get clapped: `getClapped()` - makes any number -999999999999
* Slay: `slay()` - adds '👑💅💁‍♀️' to any string
* Rahh: `rahh()` - adds '🦅🇺🇸🤠' to any string
* Let him cook: `lethimcook()` - adds '🗣👨‍🍳🍲' to any string
* Spongebob: `spongebob()` - 'MaKeS TeXt LoOk LiKe ThIs'

## Demo Code

```
yur heres a single line comment <3

yurrr
    multi
    line
    comment
yurrr

fortnite a = 7 <3   yur declares an integer
dubs b = 5.0 <3   yur declares a double

worrrd d = "our language is: " <3   yur declares string
rizzler c = 'Z' <3   yur declares character

yur use to toSlay to declare a function
toSlay function_name (a, b) {
    bussIf (a sus b) {   yur if a is not equal to b then...
        forReal(fortnite i = 0; i < 10; i++) {
            <>"Hello there " + i </> <3   yur prints "Hello there [i]", i counting from 0 to 9
        }
    } bussElse {
        <> d + c </>   yur prints "our language is: Z"
    }
}

function_name (a , b)   yur calls the function above

yur functions below explained in 'Features' section
<>a.unoReverse()</> <3
<>a.getClapped()</> <3
<>d.slang()</> <3
<>d.slay()</> <3
```

Language Grammar Definition:

```
PROGRAM ::= STATEMENT*

STATEMENT ::= VARIABLE_DECLARATION
            | FUNCTION_DECLARATION
            | FUNCTION_CALL
            | PRINT_STATEMENT
            | COMMENT

VARIABLE_DECLARATION ::= TYPE IDENTIFIER '=' EXPRESSION '<3'

TYPE ::= 'fortnite' | 'dubs' | 'worrrd' | 'rizzler'

IDENTIFIER ::= [a-zA-Z_][a-zA-Z_0-9]*

EXPRESSION ::= TERM ((ADD | SUB) TERM)*

TERM ::= FACTOR ((MUL | DIV) FACTOR)*

FACTOR ::= NUMBER | IDENTIFIER

NUMBER ::= [0-9]+ | [0-9]+ '.' [0-9]+

ADD ::= '+'
SUB ::= '-'
MUL ::= '*'
DIV ::= '/'

FUNCTION_DECLARATION ::= 'toSlay' IDENTIFIER '(' PARAMETER_LIST ')' BLOCK

PARAMETER_LIST ::= IDENTIFIER (',' IDENTIFIER)*

BLOCK ::= '{' STATEMENT* '}'

FUNCTION_CALL ::= IDENTIFIER '(' EXPRESSION (',' EXPRESSION)* ')'

PRINT_STATEMENT ::= '<>' EXPRESSION '</>' '<3'

COMMENT ::= 'yur' | 'yurrr' COMMENT_BODY

COMMENT_BODY ::= [^<3]* '<3' | [^yurrr]* 'yurrr'

BLOCK_COMMENT ::= 'yurrr' COMMENT_BODY 'yurrr'
```

## State of the Language

Currently, the Language is capable of doing simple binary operations (+ - * /). The language can split up the input code
from the genz file into the correct tokens based on our language syntax using regular expressions. The language can also handle variable declarations
for integers or doubles. The parser handles this an creates the ast tree. 

## Run 

To run a genz file, you can open it in the z#_interpret.py file, OR you can run the z#_interpret file on the command line and 
pass whatever genz file you want there. 
