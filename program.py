from parser import *
from lexer import *
lexer = Lexer()
parser = Parser(lexer)

prog = parser.parse()
print(prog.kind)