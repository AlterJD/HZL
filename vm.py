FETCH, STORE, PUSH, POP, ADD, SUB, LT, JZ, JNZ, JMP, HALT = range(11)

VMTYPES = [
  'FETCH', 'STORE', 'PUSH', 'POP', 'ADD', 'SUB', 'LT', 'JZ', 'JNZ', 'JMP', 'HALT'
]






class VM:

	def run(self, program):
		var = [0 for i in range(26)]
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

		print ('Finished execution.')
		for i in range(26):
			if var[i] != 0:
				print ('%c = %d' % (chr(i+ord('a')), var[i]))