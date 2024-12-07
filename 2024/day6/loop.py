from patrol import Guard
import sys
from copy import deepcopy


def main():
    #data = Scraper(6).getInput()
    data: list[list[str]] = [[char for char in row] for row in sys.stdin.read().split("\n")]

    guard = Guard(deepcopy(data))
    guard.solve()
    solutions = -1 # offset for the case where new block replaces guard position
    for position in guard.get_previous().keys():
        x, y = position
        new_data = deepcopy(data)
        new_data[x][y] = 'O'
        new_guard = Guard(new_data)
        value = new_guard.solve()
        #print(position, value)
        if value == 1:
            solutions += 1
            print(new_guard, "\n\n\n")
    print("solutions", solutions)

if __name__ == '__main__':
    main()
