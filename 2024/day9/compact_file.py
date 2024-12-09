import sys


def createList(line) -> list[str]:
    data = []
    for idx, num in enumerate(line):
        num = int(num)
        if not idx % 2:
            data += [idx // 2] * num
        else:
            if num >= 0:
                data += ['.'] * num
    return data


def compactList(data) -> list[str]:
    front = 0
    back = len(data) - 1
    while front <= back:

        if data[front] != '.':
            front += 1
            continue

        if data[back] == '.':
            back -= 1
            continue

        data[front], data[back] = data[back], data[front]
        front += 1
        back -= 1

    return data[:front]


def checkSum(data) -> int:
    total = 0
    for idx, value in enumerate(data):
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