import sys


def createList(line) -> list[list[str | int]]:
    data: list[list[str | int]] = []
    for idx, num in enumerate(line):
        num = int(num)
        if not idx % 2:
            data.append([idx // 2] * num)
        else:
            if num > 0:
                data.append(['.'] * num)
    return data


def compactList(data: list[list[str | int]]) -> list[str | int]:

    length = len(data)

    for back in range(length - 1, -1, -1):
        block = data[back]

        if block[0] == '.':
            continue

        for front in range(length):
            empty = data[front]

            if empty[0] != '.':
                continue

            if front >= back:
                break

            block_size = len(block)
            empty_size = len(empty)

            if empty_size >= block_size:
                data[front] = block
                data[back] = ['.'] * block_size #type: ignore

                if empty_size > block_size:
                    data.insert(front + 1, ['.'] * (empty_size - block_size))
                break

    # Flatten the list
    flattened = [item for sublist in data for item in sublist]
    return flattened


def checkSum(data) -> int:
    total = 0
    for idx, value in enumerate(data):
        if isinstance(value, int):
            total += (idx * value)
    return total


def main():
    line = sys.stdin.read().strip()

    data = createList(line)

    data = compactList(data)

    sum = checkSum(data)

    print(sum)


if __name__ == "__main__":
    main()