import sys


def oneDirection(data):
    """Check if a sequence is strictly increasing or decreasing."""
    return (all(x < y for x, y in zip(data, data[1:])) or
            all(x > y for x, y in zip(data, data[1:])))


def validDistance(data):
    """Check if the difference between adjacent levels is between 1 and 3 inclusive."""
    return all(1 <= abs(x - y) <= 3 for x, y in zip(data, data[1:]))


def isSave(data: list):
    if oneDirection(data) and validDistance(data):
        return True

    # Check if levels can be safe by removing one element
    for i in range(len(data)):
        modified_data = data[:i] + data[i + 1:]
        if oneDirection(modified_data) and validDistance(modified_data):
            return 1
    
    return 0


def main():

    save = 0
    for line in sys.stdin:
        rates = [int(num) for num in line.split()]
        save += isSave(rates)

    print(save)


if __name__ == "__main__":
    main()
