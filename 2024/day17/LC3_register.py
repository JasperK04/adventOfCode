import sys
import re

def little_computer_3(instructions: list[int], registers: list[int]) -> bool:
	index: int = 0
	output: list[int] = []

	def equal():
		if len(output) != len(instructions):
			return False
		for one, two in zip(output, instructions):
			if one != two:
				return False
		return True
			
	op_codes = {
		0: "div value a",
		1: "xor value b",
		2: "mod b % 8",
		3: "jump value",
		4: "xor b c",
		5: "out",
		6: "div b a",
		7: "div c a"
	}

	def value(num):
		if 0 <= num <= 3:
			return num
		if 4 <= num <= 6:
			return registers[num%4]
		
		raise ValueError(f"invalid operator: {num}")
	
	def div(operand, target):
		denominator = 2 ** value(operand)
		if denominator == 0:
			raise ZeroDivisionError("Division by zero")
		registers[target] = registers[0] // denominator

	def xor(second):
		registers[1] ^= second

	def mod(operand):
		registers[1] = value(operand) % 8

	def out(operand):
		output.append(value(operand) % 8)


	while index < len(instructions):
		opcode = instructions[index]
		operand = instructions[index + 1]
		print(f"current: {index}, opcode: {opcode}, value: {operand}, instruction: {op_codes[opcode]}")

		if opcode == 0:  # adv
			div(operand, 0)  # Operate on A (register 0)
		elif opcode == 1:  # bxl
			xor(operand)  # Operate on B (register 1)
		elif opcode == 2:  # bst
			mod(operand)  # Operate on B (register 1)
		elif opcode == 3:  # jnz
			if registers[0] != 0:  # Check if A (register 0) is non-zero
				index = operand
				continue  # Skip the default index increment
		elif opcode == 4:  # bxc
			xor(registers[2])  # B XOR C, ignores operand
		elif opcode == 5:  # out
			out(operand)
			if output[len(output)-1] != instructions[len(output)-1]:
				return False
		elif opcode == 6:  # bdv
			div(operand, 1)  # Operate on B (register 1)
		elif opcode == 7:  # cdv
			div(operand, 2)  # Operate on C (register 2)
		else:
			raise ValueError(f"Invalid opcode: {opcode}")
		
		index += 2

	return equal()


def main():
	data, instructions = sys.stdin.read().strip().split("\n\n", maxsplit=1)

	registers = list(map(int, re.findall(r'[0-9]+', data)))
	instructions = list(map(int, re.findall(r'[0-9]+', instructions))) 
	instructions[0] = 1

	while not little_computer_3(instructions, registers):
		instructions[0] += 1


if __name__ == "__main__":
	main()
