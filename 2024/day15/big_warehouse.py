import sys
from collections import deque


def build_grid(grid):
	new = []
	for r in grid.split('\n'):
		row = []
		for char in r:
			if char == '#':
				row.append('#')
				row.append('#')
			if char == 'O':
				row.append('[')
				row.append(']')
			if char == '.':
				row.append('.')
				row.append('.')
			if char == '@':
				row.append('@')
				row.append('.')
		new.append(row)

	max_x = len(new)
	max_y = len(new[0])
	
	return new, max_x, max_y


def find(grid, target) -> tuple[int, int] | None:
	for i, row in enumerate(grid):
		for j, char in enumerate(row):
			if char == target:
				return (i, j)
	

def move(grid, moves):
	grid, x_max, y_max = build_grid(grid)

	pos = find(grid, "@")
	assert pos, 'failed to find the robot'
	x, y = pos
	grid[x][y] = '.'

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

		elif grid[ax][ay] in ['[', ']']:
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

				elif grid[bx][by] == '[':
					queue.append((bx, by))
					assert grid[bx][by+1] == ']'
					queue.append((bx, by+1))
				elif grid[bx][by] == ']':
					queue.append((bx, by))
					assert grid[bx][by-1] == '['
					queue.append((bx, by-1))
			
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
			if grid[x][y] == '[':
				total += 100*x + y

	return total


def main():
	grid, moves = sys.stdin.read().strip().split("\n\n", maxsplit=1)
	moves = moves.replace("\n", "")
	
	value = move(grid, moves)

	print(value)


if __name__ == "__main__":
	main()
