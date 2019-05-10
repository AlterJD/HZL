from parser import *
from lexer import *
from compiler import *
from vm import *

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
compiler = Compiler()
program = compiler.compile(prog)
def Commamd(comIndex):
  if comIndex < len(VMTYPES):
    return VMTYPES[comIndex]
  else:
    return ""
i = 0
for operation in program:
  print(str(i) + ": " +str(operation) + " " + Commamd(operation))
  i = i + 1

  # {a=1;if(a>2){a=a+1;}}