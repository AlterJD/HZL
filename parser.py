import sys
from lexer import*

class Node:
	def __init__(self, kind, value = None, operand1 = None, operand2 = None, operand3 = None):
		self.kind = kind
		self.value = value
		self.operand1 = operand1
		self.operand2 = operand2
		self.operand3 = operand3

class Parser:

  VAR, CONST, ADD, SUB, LT, MT, SET, IF1, IF2, WHILE, DO, EMPTY, SEQ, EXPR, PROG = range(15)

  def __init__(self, lexer):
    self.lexer = lexer

  def error(self, msg):
    print ('Parser error:', msg)
    sys.exit(1)

  def term(self):
    if self.lexer.symbol == Lexer.ID:
      n = Node(Parser.VAR, self.lexer.value)
      self.lexer.next_token()
      return n
    elif self.lexer.symbol == Lexer.NUMBER:
      n = Node(Parser.CONST, self.lexer.value)
      self.lexer.next_token()
      return n
    else:
      return self.parent_expr()

  def sum(self):
    n = self.term()
    while self.lexer.symbol == Lexer.PLUSik or self.lexer.symbol == Lexer.MINUSik:
      if self.lexer.symbol == Lexer.PLUSik:
        kind = Parser.ADD
      else:
        kind = Parser.SUB
      self.lexer.next_token()
      n = Node(kind, operand1 = n, operand2 = self.term())
    return n

  def test(self):
    n = self.sum()
    if self.lexer.symbol == Lexer.LESS:
      self.lexer.next_token()
      n = Node(Parser.LT, operand1 = n, operand2 = self.sum())
    elif self.lexer.symbol == Lexer.MORE:
      self.lexer.next_token()
      n = Node(Parser.MT,operand1 = n, operand2 = self.sum())
    return n


  def expr(self):
    if self.lexer.symbol != Lexer.ID:
      return self.test()
    n = self.test()
    if n.kind == Parser.VAR and self.lexer.symbol == Lexer.EQUAL:
      self.lexer.next_token()
      n = Node(Parser.SET, operand1 = n, operand2 = self.expr())
    return n

  def parent_expr(self):
    if self.lexer.symbol != Lexer.LBR:
      self.error('"(" expected')
    self.lexer.next_token()
    n = self.expr()
    if self.lexer.symbol != Lexer.RBR:
      self.error('")" expected')
    self.lexer.next_token()
    return n

  def statement(self):
    if self.lexer.symbol == Lexer.IF:
      n = Node(Parser.IF1)
      self.lexer.next_token()
      n.operand1 = self.parent_expr()
      n.operand2 = self.statement()
      if self.lexer.symbol == Lexer.ELSE:
        n.kind = Parser.IF2
        self.lexer.next_token()
        n.operand3 = self.statement()
    elif self.lexer.symbol == Lexer.WHILE:
      n = Node(Parser.WHILE)
      self.lexer.next_token()
      n.operand1 = self.parent_expr()
      n.operand2 = self.statement()
    elif self.lexer.symbol == Lexer.DO:
      n = Node(Parser.DO)
      self.lexer.next_token()
      n.operand1 = self.statement()
      if self.lexer.symbol != Lexer.WHILE:
        self.error('"while" expected')
      self.lexer.next_token()
      n.operand2 = self.parent_expr()
      if self.lexer.symbol != Lexer.SCOL:
        self.error('";" expected')
    elif self.lexer.symbol == Lexer.SCOL:
      n = Node(Parser.EMPTY)
      self.lexer.next_token()
    elif self.lexer.symbol == Lexer.LB:
      n = Node(Parser.EMPTY)
      self.lexer.next_token()
      while self.lexer.symbol != Lexer.RB:
        n = Node(Parser.SEQ, operand1 = n, operand2 = self.statement())
      self.lexer.next_token()
    else:
      n = Node(Parser.EXPR, operand1 = self.expr())
      if self.lexer.symbol != Lexer.SCOL:
        self.error('";" expected')
      self.lexer.next_token()
    return n

  def parse(self):
    self.lexer.next_token()
    n = Node(Parser.PROG, operand1 = self.statement())
    if (self.lexer.symbol != Lexer.EOF):
      self.error("Invalid statement syntax")
    return n