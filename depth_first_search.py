from collections import deque

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

route_1 = deque()
explored_set_1 = set()
start_1 = 'A'

def goal_test_1(node: str):
    return node == 'O'

def dfs(path: dict, route: deque, start: str, goal_test):
    route.appendleft((start, [start]))
    explored_set = set()

    while route:
        node, path_taken = route.popleft()
        
        if node in explored_set:
            continue

        explored_set.add(node)

        if goal_test(node):
            print(f"You have reached the goal: {node}")
            print("Path taken:", " -> ".join(path_taken))
            return  

        children = path.get(node, [])
        for child in reversed(children):
            route.appendleft((child, path_taken + [child]))

        print(f"Nodes remaining: {list(n for n, _ in route)}\n")

def dls(path: dict, start: str, goal_test, depth_limit: int):
    route = deque()
    route.append((start, 0, [start]))  
    explored = set()

    while route:
        current_node, current_depth, path_taken = route.popleft()

        if goal_test(current_node):
            print(f"You have reached the goal: {current_node}")
            print("Path taken:", " -> ".join(path_taken))
            return  

        if current_depth >= depth_limit:
            continue

        if current_node not in explored:
            explored.add(current_node)

            if current_node in path:
                children = reversed(path[current_node])  

                for child in children:  
                    route.appendleft((child, current_depth + 1, path_taken + [child]))

        print(f"Nodes explored: {explored}")
        print(f"Nodes remaining: {[n for n, _, _ in route]}\n")

    print("No solution could be found within the depth limit")
    return None

def ids(path: dict, start: str, goal_test: callable, max_depth_limit: int):
    for depth_limit in range(max_depth_limit + 1):
        print(f"\nDepth Limit: {depth_limit}")
        result = dls(path, start, goal_test, depth_limit)

        if result is not None:
            return result
        
    return None
        
def main():
    """dfs(path_1,route_1, start_1, goal_test_1)"""
    dls(path_1, start_1, goal_test_1, 3) 
    """ids(path_1, start_1, goal_test_1, 4)"""

if __name__ == "__main__":
    main()