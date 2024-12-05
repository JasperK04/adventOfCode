import sys


def count_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    count = 0

    def findDiagonal(x, y, direction):
        Letters = ["M", "S"]
        first, second = direction
        
        dx, dy = first
        letter = grid[x+dx][y+dy]
        if letter not in Letters:
            return False
        Letters.remove(letter)
        
        dx, dy = second
        letter = grid[x+dx][y+dy]
        if letter in Letters:
            return True
        return False

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if grid[i][j] == "A":
                if findDiagonal(i, j, ((-1, 1), (1, -1))) and findDiagonal(i, j, ((-1, -1), (1, 1))):
                    count += 1

    return count



def main():
    grid = sys.stdin.read().splitlines()

    total_occurrences = count_occurrences(grid)
    print(f"Total occurrences: {total_occurrences}")


if __name__ == "__main__":
    main()
