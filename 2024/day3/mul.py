import re
import sys

def multiply():
    ...


def main():
    memory = sys.stdin.read()
    sums = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", memory)
    total = 0
    for sum in sums:
        nums = re.findall(r"[0-9]{1,3}", sum)
        if len(nums) != 2: continue
        total += int(nums[0]) * int(nums[1])

    print(total)



if __name__ == "__main__":
    main()