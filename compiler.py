from parser import *
from vm import *

class Compiler:
  
  program = []
  pc = 0

  def gen(self, command):
    self.program.append(command)
    self.pc = self.pc + 1
  
  def compile(self, node):
    if node.kind == Parser.VAR:
      self.gen(FETCH)
      self.gen(node.value)
    elif node.kind == Parser.CONST:
      self.gen(PUSH)
      self.gen(node.value)
    elif node.kind == Parser.ADD:
      self.compile(node.operand1)
      self.compile(node.operand2)
      self.gen(ADD)
    elif node.kind == Parser.SUB:
      self.compile(node.operand1)
      self.compile(node.operand2)
      self.gen(SUB)
    elif node.kind == Parser.LT:
      self.compile(node.operand1)
      self.compile(node.operand2)
      self.gen(LT)
    elif node.kind == Parser.MT:
      self.compile(node.operand1)
      self.compile(node.operand2)
      self.gen(MT)
    elif node.kind == Parser.SET:
      self.compile(node.operand2)
      self.gen(STORE)
      self.gen(node.operand1.value)
    elif node.kind == Parser.IF1:
      self.compile(node.operand1)
      self.gen(JZ); addr = self.pc; self.gen(0)
      self.compile(node.operand2)
      self.program[addr] = self.pc
    elif node.kind == Parser.IF2:
      self.compile(node.operand1)
      self.gen(JZ); addr1 = self.pc; self.gen(0)
      self.compile(node.operand2)
      self.gen(JMP); addr2 = self.pc; self.gen(0)
      self.program[addr1] = self.pc
      self.compile(node.operand3)
      self.program[addr2] = self.pc
    elif node.kind == Parser.WHILE:
      addr1 = self.pc
      self.compile(node.operand1)
      self.gen(JZ); addr2 = self.pc; self.gen(0)
      self.compile(node.operand2)
      self.gen(JMP); self.gen(addr1)
      self.program[addr2] = self.pc
    elif node.kind == Parser.DO:
      addr = self.pc
      self.compile(node.operand1)
      self.compile(node.operand2)
      self.gen(JNZ) 
      self.gen(addr)

    elif node.kind == Parser.FOR:
      self.compile(node.operand1)
      addr = self.pc
      self.compile(node.operand2)
      self.gen(JZ); addr1=self.pc; self.gen(0)
      self.compile(node.operand4)
      self.compile(node.operand3)
      self.gen(JMP); self.gen(addr)
      self.program[addr1]=self.pc
    
    elif node.kind == Parser.READ:
      self.gen(READLN)
      self.gen(STORE)
      self.gen(node.value)

    elif node.kind == Parser.LLPRINT:
      self.gen(LLPRINT)

    elif node.kind == Parser.HPRINT:
      self.gen(HPRINT)
    
    elif node.kind == Parser.LLADD:
      self.gen(LLADD)
      self.gen(node.value)

    elif node.kind == Parser.LLREMOVE:
      self.compile(node.operand1)
      self.gen(LLREMOVE)

    elif node.kind == Parser.LLGET:
      self.compile(node.operand1)
      self.gen(LLGET)
      self.gen(node.value)

    elif node.kind == Parser.HADD:
      self.compile(node.operand1)
      self.gen(HADD)

    elif node.kind == Parser.HREMOVE:
      self.compile(node.operand1)
      self.gen(HREMOVE)

    elif node.kind == Parser.PRINT:
      self.gen(FETCH)
      self.gen(node.value)
      self.gen(PRINTLN)

    elif node.kind == Parser.HCONTAINS:
      self.compile(node.operand1)
      self.gen(HCONTAINS)
      self.gen(node.value)
    elif node.kind == Parser.SEQ:
      self.compile(node.operand1)
      self.compile(node.operand2)
    elif node.kind == Parser.EXPR:
      self.compile(node.operand1)
      self.gen(POP)
    elif node.kind == Parser.PROG:
      self.compile(node.operand1)
      self.gen(HALT)
    return self.program