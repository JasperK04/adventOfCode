import sys
import re
from sympy import symbols, Eq, solve

class Game:
	def __init__(self, data, num=0):
		numbers = re.findall(r"[0-9]+", data)
		assert len(numbers) == 6, f"This game has invalid paramiters: {numbers}"
		a, b = symbols('A B', integer=True)
		self.symbols = a, b
		self.x = Eq(int(numbers[0]) * a + int(numbers[2]) * b, int(numbers[4])+num)
		self.y = Eq(int(numbers[1]) * a + int(numbers[3]) * b, int(numbers[5])+num)
		
		self.x_str = f"{numbers[0]}*A + {numbers[2]}*B = {int(numbers[4])+num}"
		self.y_str = f"{numbers[1]}*A + {numbers[3]}*B = {int(numbers[5])+num}"

		self.solutions = None
		self.value = 0

	def solver(self):
		if not self.solutions:
			sol = solve((self.x, self.y), self.symbols)
			self.solutions = sol
		if sol:
			self.value = sol[self.symbols[0]] * 3 + sol[self.symbols[1]] * 1
		return self.value

	def __str__(self):
		return self.x_str + "\n" + self.y_str

def main():
	data = sys.stdin.read().strip().split("\n\n")

	total1 = 0
	total2 = 0
	for machine in data:
		total1 += Game(machine).solver()
		total2 += Game(machine, 10_000_000_000_000).solver()

	print("1:", total1)
	print("2:",total2)
	

if __name__ == "__main__":
	main()
