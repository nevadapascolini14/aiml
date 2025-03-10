from collections import deque

def dfs(path: dict, start: str, goal_test: callable):
    """Tree variety depth-first search of a state space for a goal condition.

    Args:
        path (dict): A dictionary representing pathways between states
        start (str): The initial state
        goal_test (callable): A function that checks if a state is a goal state
    """
    route = deque()
    route.appendleft((start, [start]))
    print(f"Starting DFS from {start}")

    while route:
        node, path_taken = route.popleft()
        print(f"Exploring Node: {node}, Path: {' -> '.join(path_taken)}")

        if goal_test(node):
            print(f"Goal reached: {node}")
            print("Final Path:", " -> ".join(path_taken))
            return

        children = path.get(node, [])
        print(f"Expanding {node}, adding children: {children}")
        for child in reversed(children):
            route.appendleft((child, path_taken + [child]))

        print(f"Queue State: {list(n for n, _ in route)}\n")


def dls(path: dict, start: str, goal_test: callable, depth_limit: int):
    """Tree variety depth-limited search of a state space for a goal condition.

    Args:
        path (dict): A dictionary representing pathways between states.
        start (str): The initial state.
        goal_test (callable): A function that checks if a state is a goal state.
        depth_limit (int): The limit of depth of node to search before terminating.

    Returns:
        None: If no solution is found.
    """
    route = deque()
    route.append((start, 0, [start]))
    print(f"Starting DLS with depth limit {depth_limit}")

    while route:
        current_node, current_depth, path_taken = route.popleft()
        print(
            f"Exploring Node: {current_node}, Depth: {current_depth}, Path: {' -> '.join(path_taken)}"
        )

        if goal_test(current_node):
            print(f"Goal reached: {current_node}")
            print("Final Path:", " -> ".join(path_taken))
            return

        if current_depth >= depth_limit:
            print(
                f"Reached depth limit at node {current_node}, skipping further expansion."
            )
            continue

        if current_node in path:
            children = reversed(path[current_node])
            print(f"Expanding {current_node}, adding children: {list(children)}")
            for child in children:
                route.appendleft((child, current_depth + 1, path_taken + [child]))

        print(f"Queue State: {[n for n, _, _ in route]}")

    print("No solution found within the depth limit")
    return None


def ids(path: dict, start: str, goal_test: callable, max_depth_limit: int):
    """Tree variety iterative-deepening search of a state space for a goal condition.

    Args:
        path (dict): A dictionary representing pathways between states.
        start (str): The initial state.
        goal_test (callable): A function that checks if a state is a goal state.
        max_depth_limit (int): The limit of depth of node to search before terminating.

    Returns:
        None: If no solution is found
    """
    print("Starting IDS...")
    for depth_limit in range(max_depth_limit + 1):
        print(f"\nRunning DLS with Depth Limit: {depth_limit}")
        result = dls(path, start, goal_test, depth_limit)

        if result is not None:
            return result

    return None


def main():
    path_1 = {
        "A": ["B", "C", "D"],
        "B": ["E", "F"],
        "C": ["G"],
        "D": ["H", "I", "J"],
        "E": ["K", "L"],
        "F": ["N"],
        "I": ["O"],
        "L": ["M"],
    }

    def goal_test_1(node: str):
        return node == "O"

    # ids(path_1, "A", goal_test_1, 4)
    dfs(path_1, "A", goal_test_1)

if __name__ == "__main__":
    main()
