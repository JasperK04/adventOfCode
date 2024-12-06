from collections import defaultdict, deque
import sys

def parse_input(input_data):
    rules, updates = input_data.strip().split("\n\n")

    # Parse rules
    order_rules = []
    for line in rules.split("\n"):
        x, y = map(int, line.split("|"))
        order_rules.append((x, y))

    # Parse updates
    updates_list = []
    for line in updates.split("\n"):
        updates_list.append(list(map(int, line.split(","))))

    return order_rules, updates_list


def build_graph(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0

    return graph, in_degree


def topological_sort(subset, graph, in_degree):
    # Create a subgraph only for the subset of pages
    subset_graph = defaultdict(list)
    subset_in_degree = {node: 0 for node in subset}

    for node in subset:
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in subset:
                    subset_graph[node].append(neighbor)
                    subset_in_degree[neighbor] += 1

    # Perform Kahn's Algorithm
    queue = deque([node for node in subset if subset_in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in subset_graph[current]:
            subset_in_degree[neighbor] -= 1
            if subset_in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


def find_middle_pages_sum(rules, updates):
    # Build the graph and in-degree map
    graph, in_degree = build_graph(rules)

    middle_sum = 0
    for update in updates:
        is_valid = True

        # Check if the update is valid
        for x in update:
            for y in update:
                if y in graph[x] and update.index(x) > update.index(y):
                    is_valid = False
                    break

        if not is_valid:
            # Reorder the update
            update = topological_sort(update, graph, in_degree)

            # Find the middle page
            middle_sum += update[len(update) // 2]

    return middle_sum


def main():

    rules, updates = parse_input(sys.stdin.read())
    result = find_middle_pages_sum(rules, updates)
    print("Sum of middle pages after reordering:", result)

if __name__ == "__main__":
    main()
