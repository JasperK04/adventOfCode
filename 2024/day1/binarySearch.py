import sys

class SortedList(list):
    def __init__(self, *args):
        """Initialize the heap with optional initial values."""
        if args:
            super().__init__(*args)
            self.merge_sort()
        else:
            super().__init__()

    def add(self, value):
        """Add an element to the list and keep it sorted using insertion sort logic."""
        self.append(value)
        # Perform insertion sort on the newly added element
        i = len(self) - 1
        while i > 0 and self[i] < self[i - 1]:
            self[i], self[i - 1] = self[i - 1], self[i]
            i -= 1

    def merge_sort(self):
        """Sort the list using merge sort algorithm."""
        if len(self) <= 1:
            return self

        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        def merge_sort_recursive(lst):
            if len(lst) <= 1:
                return lst
            mid = len(lst) // 2
            left = merge_sort_recursive(lst[:mid])
            right = merge_sort_recursive(lst[mid:])
            return merge(left, right)

        sorted_list = merge_sort_recursive(self)
        self[:] = sorted_list  # Update the current list with the sorted one
        return self

    def binary_search(self, target):
        """Perform binary search on the sorted list."""
        left, right = 0, len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self[mid] == target:
                return mid
            elif self[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Element not found


def main():
    list_1 = []
    list_2 = []
    for line in sys.stdin:
        first, second = line.split(maxsplit=1)
        list_1.append(int(first.strip()))
        list_2.append(int(second.strip()))
    list_2 = SortedList(list_2)
    
    distance = 0
    length = len(list_1)
    for _ in range(length):
        num = list_1.pop()
        idx = list_2.binary_search(num)
        if idx < 0:
            continue
        min = max = idx
        while num == list_2[min]:
            min -= 1
        min += 1
        while num == list_2[max]:
            max += 1
        distance += num * (max - min)

    print(distance)


if __name__ == "__main__":
    main()