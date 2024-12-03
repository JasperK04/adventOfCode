import re
import sys

def multiply():
    ...


def main():
    memory = sys.stdin.read()
    do = r"do\(\)"
    dont = r"don\'t\(\)"
    mul = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"
    pattern = '|'.join([do, dont, mul])

    operators = re.findall(pattern, memory)
    total = 0
    active = True
    for operator in operators:
        if operator == "don't()":
            active = False
            continue
        if operator == "do()":
            active = True
        if active:
            nums = re.findall(r"[0-9]{1,3}", operator)
            if len(nums) != 2: continue
            total += int(nums[0]) * int(nums[1])

    print(total)



if __name__ == "__main__":
    main()