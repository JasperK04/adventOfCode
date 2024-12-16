import sys
from min_heap import minHeap

def parse_maze(maze):
	start = None
	end = None
	grid = []

	for r, row in enumerate(maze):
		grid_row = []
		for c, cell in enumerate(row):
			if cell == 'S':
				start = (r, c, 'EAST')  # Start position with heading south
				grid_row.append('.')
			elif cell == 'E':
				end = (r, c)
				grid_row.append('.')
			else:
				grid_row.append(cell)
		grid.append(grid_row)

	for row in grid:
		print(''.join(row))

	return grid, start, end


def dijkstra(maze, start, end):
	# setup
	directions = {
		'NORTH': (-1, 0),
		'EAST': (0, 1),
		'SOUTH': (1, 0),
		'WEST': (0, -1)
	}
	turn_cost = 1000
	turns = {
		'NORTH': {'LEFT': 'WEST', 'RIGHT': 'EAST'},
		'EAST': {'LEFT': 'NORTH', 'RIGHT': 'SOUTH'},
		'SOUTH': {'LEFT': 'EAST', 'RIGHT': 'WEST'},
		'WEST': {'LEFT': 'SOUTH', 'RIGHT': 'NORTH'}
	}
	rows, cols = len(maze), len(maze[0])
	
	# heapqueue initialization
	queue = minHeap()
	queue.push((0, start[0], start[1], start[2]))  # (cost, row, col, heading)
	visited = set()

	while queue:
		cost, r, c, heading = queue.pop()
		#print(cost, r, c, heading)
		
		if (r, c, heading) in visited:
			#print("already visited:", (r, c, heading))
			continue
		visited.add((r, c, heading))

		if (r, c) == end:
			return cost

		dr, dc = directions[heading]
		nr, nc = r + dr, c + dc
		if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
			#print(nr, nc)
			queue.push((cost + 1, nr, nc, heading))

		for new_heading in [turns[heading]['LEFT'], turns[heading]['RIGHT']]:
			#print(r, c, new_heading)
			queue.push((cost + turn_cost, r, c, new_heading))

	return -1  # If no path exists


def main():
	data = sys.stdin.read().strip().split("\n")
     
	maze, start, end = parse_maze(data)

	distance = dijkstra(maze, start, end)
	print(distance)


if __name__ == "__main__":
	main()
