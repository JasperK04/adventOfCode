import sys


def main():
    order_dict = {}
    ordering, rules = sys.stdin.read().split('\n\n', 1)
    for order in ordering.split('\n'):
        key, value = order.strip().split('|')
        order_dict.setdefault(value, []).append(key)

    sum = 0
    for line in rules.split("\n"):
        seen = []
        values = line.strip().split(",")
        for value in values:
            if value in seen:
                break
            else:
                seen += order_dict.get(value, [])
        else:
            sum += int(values[len(values)//2])

    print(sum)


    print(order_dict)

if __name__ == "__main__":
    main()
