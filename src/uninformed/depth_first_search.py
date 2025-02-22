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

    while route:
        node, path_taken = route.popleft()

        if goal_test(node):
            print(f"You have reached the goal: {node}")
            print("Path taken:", " -> ".join(path_taken))
            return  

        children = path.get(node, [])
        for child in reversed(children):
            route.appendleft((child, path_taken + [child]))

        print(f"Nodes remaining: {list(n for n, _ in route)}\n")

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

    while route:
        current_node, current_depth, path_taken = route.popleft()

        if goal_test(current_node):
            print(f"You have reached the goal: {current_node}")
            print("Path taken:", " -> ".join(path_taken))
            return  

        if current_depth >= depth_limit:
            continue

        if current_node in path:
            children = reversed(path[current_node])  

            for child in children:  
                route.appendleft((child, current_depth + 1, path_taken + [child]))

        print(f"Nodes remaining: {[n for n, _, _ in route]}\n")

    print("No solution could be found within the depth limit")
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
    for depth_limit in range(max_depth_limit + 1):
        print(f"\nDepth Limit: {depth_limit}")
        result = dls(path, start, goal_test, depth_limit)

        if result is not None:
            return result
        
    return None
        
def main():
    
    path_1 = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H', 'I', 'J'],
        'E': ['K', 'L'],
        'F': ['N'],
        'I': ['O'],
        'L': ['M']
    }

    def goal_test_1(node: str):
        return node == 'O'
    
    """dfs(path_1, 'A', goal_test_1)"""
    """dls(path_1, 'A', goal_test_1, 3)"""
    ids(path_1, 'A', goal_test_1, 4)

if __name__ == "__main__":
    main()