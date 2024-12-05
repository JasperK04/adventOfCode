import sys

def count_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Diagonal down-right
        (1, -1),  # Diagonal down-left
    ]
    count = 0

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_direction(x, y, dx, dy, word):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not in_bounds(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":
                for dx, dy in directions:
                    if search_direction(i, j, dx, dy, word):
                        count += 1
            elif grid[i][j] == "S":
                for dx, dy in directions:
                    if search_direction(i, j, dx, dy, word[::-1]):
                        count += 1

    return count


def main():
    grid = sys.stdin.read().splitlines()
    word = "XMAS"

    total_occurrences = count_occurrences(grid, word)
    print(f"Total occurrences of '{word}': {total_occurrences}")


if __name__ == "__main__":
    main()
