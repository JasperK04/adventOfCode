import sys
import re

def findTotal(target: int, current: int, numbers: list[int]) -> int:
    if current == target:
        return current
    if not numbers or current > target:
        return 0
    temp = current * numbers[0]
    value = findTotal(target, temp, numbers[1:])
    if value:
        return value
    temp = current + numbers[0]
    value = findTotal(target, temp, numbers[1:])
    if value:
        return value
    return 0


def main():
    sum = 0
    data = sys.stdin.read().strip().split("\n")
    for line in data:
        total, *numbers = re.findall(r"[0-9]+" ,line)
        numbers = [int(num) for num in numbers]
        sum += findTotal(int(total), numbers[0], numbers[1:])
    
    print(sum)


if __name__ == "__main__":
    main()