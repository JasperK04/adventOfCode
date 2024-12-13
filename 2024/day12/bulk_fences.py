import sys
from collections import deque


def findPerimiter(grid: list[list[str]]) -> int:
    visited: set[tuple[int, int]] = set()
    queue = deque()

    def BFS(pos) -> tuple[int, int]:
        area = 0
        queue.append(pos)
        perimiter = {}

        while queue:
            x, y = queue.popleft()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))
            area += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == grid[x][y]:
                    queue.append((nx, ny))
                else:
                    if (dx, dy) not in perimiter:
                        perimiter[(dx, dy)] = set()
                    perimiter[(dx, dy)].add((x, y))

        sides: int = 0
        for values in perimiter.values():
            seen_sides = set()
            for (x, y) in values:
                if (x, y) in seen_sides:
                    continue

                sides += 1
                queue2 = deque([(x, y)])
                while queue2:
                    x2, y2 = queue2.popleft()
                    if (x2, y2) in seen_sides:
                        continue
                    seen_sides.add((x2, y2))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x2 + dx, y2 + dy
                        if (nx, ny) in values:
                            queue2.append((nx, ny))

        return sides, area


    price = 0
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if (x, y) in visited:
                continue

            sides, area = BFS((x, y))
            price += sides * area
    
    return price

def main():
    data: list[list[str]] = [[char for char in row]
                             for row in sys.stdin.read().strip().split("\n")]
    
    price = findPerimiter(data)

    print(price)
    
        
if __name__ == "__main__":
    main()