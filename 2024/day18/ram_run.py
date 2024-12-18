import sys
from min_heap import minHeap

def dijkstra(maze, size):
	# setup
	directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	
	# heapqueue initialization
	queue = minHeap()

	queue.push((0, 0, 0)) # cost, x, y
	visited = set()

	while queue:
		cost, x, y = queue.pop()

		if (x, y) in visited: 
			continue
		visited.add((x, y))

		if (x, y) == (size, size):
			return cost

		for dx, dy in directions:
			nx, ny = x+dx, y+dy
			if 0 <= nx <= size and 0 <= ny <= size and maze[nx][ny] == '.' and (nx, ny) not in visited:
				queue.push((cost + 1, nx, ny))

	return -1  # If no path exists

def main():
	data = sys.stdin.read().strip().split("\n")

	#size = 7
	size = 71
	maze: list[list[str]] = [["." for _ in range(size)] for _ in range(size)]

	idx, limit = 0, 1024
	while idx < limit:
		x, y = ((size-int(num)-1) for num in data[idx].split(',', maxsplit=1))
		maze[x][y] = '#'
		idx += 1

	print('part 1:', dijkstra(maze, size-1))

	# for line in maze:
	# 	print(''.join(line))

	limit = len(data) - 1
	while idx < limit:
		x, y = ((size-int(num)-1) for num in data[idx].split(',', maxsplit=1))
		maze[x][y] = '#'
		if dijkstra(maze, size-1) == -1:
			for line in maze:
				print(''.join(line))
			print(f'part 2: {data[idx]}')
			break
		idx += 1


if __name__ == "__main__":
	main()
