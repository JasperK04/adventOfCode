import sys

Iterations = 25 # specifies number of iterations of rule application

def applyStoneRules(data: list[str]):
    memo = {}  # Cache for storing results of expensive operations
    
    for _ in range(Iterations):
        idx = 0
        new_data = []  # We will collect the new elements here to avoid inserting during the iteration
        
        while idx < len(data):
            num = data[idx]

            if num in memo:  # Check if the split for this number has been cached
                new_data += memo[num]
                idx += 1
                continue

            # Rule 1: If the number is '0', change it to '1'
            if num == '0':
                new_data.append('1')
                idx += 1

            # Rule 2: If the number has an even length, split it
            elif len(num) % 2 == 0:
                mid = len(num) // 2
                first_half = num[:mid]
                second_half = num[mid:].lstrip('0') or '0'  # Strip leading zeros from the second half
                memo[num] = [first_half, second_half]  # Store the split in cache
                new_data += memo[num]
                idx += 1

            # Rule 3: Otherwise, multiply the number by 2024
            else:
                result = str(int(num) * 2024)
                memo[num] = [result]  # Cache the multiplication result
                new_data.append(result)
                idx += 1

        # After processing all elements, we replace the data list with the new list
        data = new_data

    return data


def main():
    data = sys.stdin.read().strip().split()
    print(data)

    data = applyStoneRules(data)

    print(len(data))


if __name__ == "__main__":
    main()