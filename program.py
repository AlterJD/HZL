from parser import *
from lexer import *
lexer = Lexer()
parser = Parser(lexer)

def printNode(node, deep):
  if node.kind != Parser.EMPTY:
    print("-"*deep + Parser.TYPES[node.kind])
    if node.operand1:
      printNode(node.operand1, deep + 1)
    if node.operand2:
      printNode(node.operand2, deep + 1)
    if node.operand3:
     printNode(node.operand3, deep + 1)

prog = parser.parse()
printNode(prog, 0)


