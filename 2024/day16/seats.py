import sys
from min_heap import minHeap
sys.setrecursionlimit(10**6)

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
	visited = {}
	predecessors = {}  # Track predecessors for path reconstruction

	min_cost = float(100_000_000)
	best_end_states = []
	previous = (0, 0)

	while queue:
		cost, r, c, heading = queue.pop()
		
		if (r, c, heading) in visited and visited[(r, c, heading)] <= cost:
			continue
		visited[(r, c, heading)] = cost

		# Record predecessor
		if previous != (0, 0):
			if (r, c) not in predecessors:
				predecessors[(r, c)] = []
			predecessors[(r, c)].append((previous[0], previous[1], heading, cost))
		previous = (r, c)

		if (r, c) == end:
			if cost < min_cost:
				min_cost = cost
				best_end_states = [(r, c, heading)]
			elif cost == min_cost:
				best_end_states.append((r, c, heading))
			continue

		dr, dc = directions[heading]
		nr, nc = r + dr, c + dc
		if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
			queue.push((cost + 1, nr, nc, heading))

		for new_heading in [turns[heading]['LEFT'], turns[heading]['RIGHT']]:
			queue.push((cost + turn_cost, r, c, new_heading))

	print("done")
	# Reconstruct paths
	best_path_tiles = set()
	visited_tiles = set()  # Avoid duplicate tile exploration during backtracking

	def backtracking(r, c):
		if (r, c) in visited_tiles:
			return
		visited_tiles.add((r, c))
		best_path_tiles.add((r, c))
		if (r, c) in predecessors:
			for pr, pc, _, _ in predecessors[(r, c)]:
				if (pr, pc) in visited_tiles:
					continue
				backtracking(pr, pc)

	# Initiate backtracking from all best end states
	for r, c, _ in best_end_states:
		backtracking(r, c)

	return min_cost, best_path_tiles


def main():
	data = sys.stdin.read().strip().split("\n")
     
	maze, start, end = parse_maze(data)

	cost, best_tiles = dijkstra(maze, start, end)
	print(cost)
	print(len(best_tiles))


if __name__ == "__main__":
	main()
