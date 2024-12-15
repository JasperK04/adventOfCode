import sys
from collections import deque


def find(grid, target) -> tuple[int, int] | None:
	for i, row in enumerate(grid):
		for j, char in enumerate(row):
			if char == target:
				return (i, j)
	

def move(pos, grid, moves):
	x, y = pos
	grid[x][y] = '.'
	x_max = len(grid)
	y_max = len(grid[0])

	dirs = {
		">": (0, 1),
		"<": (0, -1),
		"^": (-1, 0),
		"v": (1, 0)
	}

	for move in moves:
		dx, dy = dirs[move]
		ax, ay = x+dx, y+dy

		if grid[ax][ay] == '#':
			continue

		elif grid[ax][ay] == '.':
			x, y = ax, ay

		elif grid[ax][ay] == 'O':
			queue = deque([(x, y)])
			seen = set()
			wall = False

			while queue:
				ax, ay = queue.popleft()
				if (ax, ay) in seen:
					continue
				seen.add((ax, ay))
				bx, by = ax+dx, ay+dy

				if grid[bx][by] == '#':
					wall = True
					break

				elif grid[bx][by] == 'O':
					queue.append((bx, by))
			
			if wall:
				continue

			while len(seen) > 0:
				for ax, ay in sorted(seen):
					bx, by = ax+dx, ay+dy
					if (bx, by) not in seen:
						assert grid[bx][by] == '.'
						grid[bx][by] = grid[ax][ay]
						grid[ax][ay] = '.'
						seen.remove((ax, ay))

			x = x+dx
			y = y+dy

	total = 0
	for x in range(x_max):
		for y in range(y_max):
			if grid[x][y] == 'O':
				total += 100*x + y

	return total


def main():
	grid, moves = sys.stdin.read().strip().split("\n\n", maxsplit=1)

	grid = [[char for char in row] for row in grid.split()]
	moves = moves.replace("\n", "")

	robot = find(grid, "@")
	if not robot:
		print("failed")
		exit(-1)
	
	value = move(robot, grid, moves)

	print(value)


if __name__ == "__main__":
	main()
