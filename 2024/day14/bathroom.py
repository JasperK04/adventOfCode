import sys
import re

class bot:
	def __init__(self, pos, speed, max):

		self.pos = pos
		self.speed = speed
		self.max = max


	def move(self, iter):
		x, y = self.pos
		dx, dy = self.speed
		max_x, max_y = self.max
		self.pos = (x + (dx * iter)) % max_x, (y + (dy * iter)) % max_y


class HQ:
	def __init__(self, data, size=(101, 103)):
		self.bots: list[bot] = []
		for line in data:
			nums = [int(num) for num in re.findall(r"[\-0-9]+", line)]
			assert len(nums) == 4, (f"invalid number of parameters in {line}")
			self.bots.append(bot((nums[0], nums[1]), (nums[2], nums[3]), size))
		
		self.size = size


	def print(self):
		posses = {}
		for bot in self.bots:
			if bot.pos in posses:
				posses[bot.pos] += 1
			else:
				posses[bot.pos] = 1

		string = ''
		for y in range(self.size[1]):
			for x in range(self.size[0]):
				if (x, y) in posses:
					string += str(posses[(x, y)])
				else:
					string += "0"
			string += '\n'

		print(string)


	def move_bots(self, iter):
		for i, _ in enumerate(self.bots):
			self.bots[i].move(iter)

	def solve(self):
		mid_row = self.size[0] // 2
		mid_col = self.size[1] // 2

		I, II, III, IIII = 0, 0, 0, 0
		for bot in self.bots:
			x, y = bot.pos
			if x < mid_col and y < mid_row:
				I += 1
			elif x > mid_col and y < mid_row:
				II += 1
			elif x < mid_col and y > mid_row:
				III += 1
			elif x > mid_col and y > mid_row:
				IIII += 1

		print(f"Midpoints: Row {mid_row}, Col {mid_col}")
		print(f"Quadrant Counts: I={I}, II={II}, III={III}, IIII={IIII}")

		return I * II * III * IIII


def main():
	data = sys.stdin.read().strip().split("\n")

	hq = HQ(data)

	hq.print()

	hq.move_bots(99)

	hq.print()

	print(hq.solve())


if __name__ == "__main__":
	main()
