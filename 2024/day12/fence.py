import sys
from collections import deque


def findPerimiter(grid: list[list[str]]) -> int:
    visited: set[tuple[int, int]] = set()
    queue = deque()

    def BFS(pos, char) -> tuple[int, int]:
        queue.append(pos)
        visited.add(pos)
        perimeter: int = 0
        area: int = 0

        while queue:
            x, y = queue.popleft()
            area += 1

            # Check all 4 neighboring cells
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    perimeter += 1
                
                elif grid[nx][ny] != char:
                    perimeter += 1

                elif (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return perimeter, area

    price = 0
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if (x, y) not in visited:
                perimiter, area = BFS((x, y), char)
                price += perimiter * area
    
    return price

def main():
    data: list[list[str]] = [[char for char in row]
                             for row in sys.stdin.read().strip().split("\n")]
    
    price = findPerimiter(data)

    print(price)
    
        
if __name__ == "__main__":
    main()