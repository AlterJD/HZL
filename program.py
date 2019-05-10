from parser import *
from lexer import *
from compiler import *
from vm import *

if len(sys.argv)<2:
  print('Please, add your program PATH')
  sys.exit(1)

with open(sys.argv[1], 'r') as content_file:
  content = content_file.read()

lexer = Lexer(content)
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

i = 0
while i < len(program):
  operation = VMTYPES[program[i]]
  if operation in VMTYPESWithARG:
    print(str(i) + ": " + operation)
    i += 1
    print(str(i) + ": " + str(program[i]))
    i +=1
  else:
    print(str(i) + ": " + operation)
    i = i + 1

vm = VM()
vm.run(program)
  # { a=1; while(a<5) {a=a+1;} }