import sys

def solve(data, iter):

    memo = {}
    def applyStoneRules(num: int, iter: int):

        # basecases
        if (num, iter) in memo:  # Check if the split for this number has been cached
            return memo[(num, iter)]
        if iter == 0:
            return_value = 1

        # Rule 1: If the number is '0', change it to '1'
        elif num == 0:
            return_value = applyStoneRules(1, iter-1)

        # Rule 2: If the number has an even length, split it
        elif len(str(num)) % 2 == 0:
            num_str = str(num)
            mid = len(num_str) // 2
            left = num_str[:mid]
            right = num_str[mid:]
            left, right = (int(left), int(right))
            return_value = applyStoneRules(left, iter-1) + applyStoneRules(right, iter-1)

        # Rule 3: Otherwise, multiply the number by 2024
        else:
            return_value = applyStoneRules(num * 2024, iter-1)

        memo[(num, iter)] = return_value
        return return_value

    return sum(applyStoneRules(num, iter) for num in data)


def main():

    sys.setrecursionlimit(10**6)
    data = [int(num) for num in sys.stdin.read().strip().split()]

    value = solve(data, 75)

    print(value)


if __name__ == "__main__":
    main()