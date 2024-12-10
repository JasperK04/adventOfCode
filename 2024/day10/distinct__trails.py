import sys
from collections import defaultdict

def findStart(grid: list[list[int]]) -> list[tuple[int, int]]:
    starts = []
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if num == 0:
                starts.append((i, j))
    return starts


def walkTrail(grid:list[list[int]], starts: list[tuple[int, int]]) -> int:

    distinct = defaultdict(int)
    
    def walkRecursive(position: tuple[int, int]) -> None:
        x, y = position
        
        # Check if the current position is a 9
        if grid[x][y] == 9:
            distinct[(x, y)] += 1
        
        # Explore neighbors (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the neighbor is within bounds
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                # Check if the neighbor is unvisited and its height is exactly one greater
                if grid[nx][ny] == grid[x][y] + 1:
                    walkRecursive((nx, ny))
        
        return

    for start in starts:
        walkRecursive(start)

    routes = 0
    for pos_count in distinct.values():
        routes += pos_count

    return routes


def main():
    data: list[list[int]] = [[int(num) for num in row]
                             for row in sys.stdin.read().strip().split("\n")]
    
    starts = findStart(data)

    trails = walkTrail(data, starts)

    print(trails)




if __name__ == "__main__":
    main()