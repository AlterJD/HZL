# -*- coding: utf-8 -*-
from linkedList import * 

FETCH, STORE, PUSH, POP, ADD, SUB, LT, MT, JZ, JNZ, JMP, HALT, READLN, PRINTLN, LLPRINT = range(15)

VMTYPES = [
  'FETCH', 'STORE', 'PUSH', 'POP', 'ADD', 'SUB', 'LT', 'MT', 'JZ', 'JNZ', 'JMP', 'HALT', 'READLN', 'PRINTLN', 'LLPRINT'
]

VMTYPESWithARG = [
  'FETCH', 'STORE', 'PUSH', 'JZ', 'JNZ', 'JMP'
]

# FETCH x - положить на стек значение переменной x
# STORE x - сохранить в переменной x значение с вершины стека
# PUSH  n - положить число n на вершину стека
# POP     - удалить число с вершины стека
# ADD     - сложить два числа на вершине стека
# SUB     - вычесть два числа на вершине стека
# LT      - сравнить два числа с вершины стека (a < b). Результат - 0 или 1
# JZ    a - если на вершине стека 0 - перейти к адресу a.
# JNZ   a - если на вершине стека не 0 - перейти к адресу a.
# JMP   a - перейти к адресу a
# HALT    - завершить работу


class VM:

  def run(self, program):
    var = [0 for i in range(26)]
    

    llist = LinkedList()
    llist.addToEnd("Tom")
    llist.addToEnd("Jack")
    llist.addToEnd("Zumba")

    stack = []
    pc = 0
    while True:
      op = program[pc]
      if pc < len(program) - 1:
        arg = program[pc+1]

      if op == FETCH: stack.append(var[arg]); pc += 2
      elif op == STORE: var[arg] = stack.pop(); pc += 2
      elif op == PUSH: stack.append(arg); pc += 2
      elif op == POP: stack.append(arg); stack.pop(); pc += 1
      elif op == ADD: stack[-2] += stack[-1]; stack.pop(); pc += 1
      elif op == SUB: stack[-2] -= stack[-1]; stack.pop(); pc += 1
      elif op == LT: 
        if stack[-2] < stack[-1]:
          stack[-2] = 1
        else:
          stack[-2] = 0
        stack.pop(); pc += 1
      elif op == MT: 
        if stack[-2] > stack[-1]:
          stack[-2] = 1
        else:
          stack[-2] = 0
        stack.pop(); pc += 1
      elif op == JZ: 
        if stack.pop() == 0:
          pc = arg
        else:
          pc += 2
      elif op == JNZ: 
        if stack.pop() != 0:
          pc = arg
        else:
          pc += 2
      elif op == JMP: pc = arg
      elif op == HALT: break
      elif op == READLN: stack.append(int(input())); pc += 1
      elif op == PRINTLN: print(str(stack.pop())); pc += 1
      elif op == LLPRINT: llist.LLprint(); pc += 1      

    print ('Shinobi execution.')
    for i in range(26):
      if var[i] != 0:
        print ('%c = %d' % (chr(i+ord('a')), var[i]))