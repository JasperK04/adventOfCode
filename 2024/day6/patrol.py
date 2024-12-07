from typing import Literal, Tuple
#from scraper import Scraper
import sys

class Guard():
    def __init__(self, grid: list[list[str]], start: Literal['up', 'right', 'down', 'left'] = 'up'):
        if start in ['up', 'right', 'down', 'left']:
            self.direction: Literal['up', 'right', 'down', 'left'] = start
        else:
            self.direction: Literal['up', 'right', 'down', 'left'] = 'up'

        self.grid = grid
        self.x, self.y = self.findGuard()
        self.dirs = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1)
        }

        self.previous: dict[Tuple[int, int], set[Literal['up', 'right', 'down', 'left']]] = {}

    def findGuard(self) -> Tuple[int, int]:
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):
                if self.grid[i][j] == '^':
                    return i, j
        return 0, 0
    
    def count(self, char) -> int:
        total = 0
        for row in self.grid:
            total += row.count(char)
        return total
        
    def turn(self) -> None:
        next = {
            "up": "right",
            "right": "down",
            "down": "left",
            "left": "up"
        }
        self.direction = next[self.direction] #type: ignore

    def go(self) -> int:
        x, y = self.dirs[self.direction]
        try:
            char = self.grid[self.x + x][self.y + y]
            if char in ["#", "O"]:
                self.turn()
                return 0
            if self.x + x < 0 or self.y + y < 0:
                raise IndexError("out of bounds")
            assert self.direction not in self.previous.get((self.x, self.y), [])
            self.grid[self.x][self.y] = "X"
            self.previous[(self.x, self.y)] = self.previous.get((self.x, self.y), set())
            self.previous[(self.x, self.y)].add(self.direction)
            self.x = self.x + x
            self.y = self.y + y
            self.grid[self.x][self.y] = "^"
            return 0
        except IndexError:
            self.grid[self.x][self.y] = "X"
            return self.count("X")
        except AssertionError:
            print("loop", end=' ')
            return 1
        
    def solve(self) -> int:
        num = 20000
        while num > 0:
            value = self.go()
            if value != 0:
                return value
            num -= 1
        return 1

    def __str__(self):
        string = ''
        for row in self.grid:
            for char in row:
                string += char
            string += "\n"
        return string.strip()
    
    def get_previous(self) -> dict[Tuple[int, int], set[Literal['up', 'right', 'down', 'left']]]:
        return self.previous

def main():
    #data = Scraper(6).getInput()
    data = [[char for char in row] for row in sys.stdin.read().split("\n")]

    guard = Guard(data)
    print(guard.solve())

if __name__ == "__main__":
    main()
