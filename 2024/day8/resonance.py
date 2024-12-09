
import sys


def findAntenna(grid: list[list[str]]) -> dict[str, set[tuple[int, int]]]:
    antennas = {}
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item != '.':
                antennas[item] = antennas.get(item, set())
                antennas[item].add((i, j))
    return antennas


def findAntinode(indexes: list, limits) -> set[tuple[int, int]]:
    
    def valid(pos_x, pos_y):
        return 0 <= pos_x < limits[0] and 0 <= pos_y < limits[1]

    positions = set()
    length = len(indexes)
    for i in range(length - 1):
        for j in range(i + 1, length):
            x1, y1 = indexes[i]
            x2, y2 = indexes[j]

            dx, dy = x1 - x2, y1 - y2

            # First antinode
            ax, ay = x1 + dx, y1 + dy
            while valid(ax, ay):
                positions.add((ax, ay))
                ax, ay = ax + dx, ay + dy

            # Second antinode
            bx, by = x2 - dx, y2 - dy
            while valid(bx, by):
                positions.add((bx, by))
                bx, by = bx - dx, by - dy

    return positions


def printNodes(grid, uniques):
    x = y = 0
    for unique in uniques:
        x, y = unique
        if grid[x][y] == ".":
            grid[x][y] = "#"
    
    for line in grid:
        print(''.join(line))
        

def main():
    uniques = set()
    data: list[list[str]] = [[char for char in row] for row in sys.stdin.read().strip().split("\n")]
    max_x = len(data[0])
    max_y = len(data)
    limits = (max_x, max_y)

    positions = findAntenna(data)

    for indexes in positions.values():
        uniques.update(indexes)
        if len(indexes) > 1:
            uniques.update(findAntinode(list(indexes), limits))

    print(len(uniques))

    printNodes(data, uniques)

if __name__ == "__main__":
    main()
