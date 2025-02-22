def bidirectional_search(graph: dict, start: str, goal: str):
    """Performs a bidirectional search for a goal state in a graph.

    Args:
        graph (dict): A dictionary representing pathways between states
        start (str): The initial state
        goal (str): The goal state

    Returns:
        List or None: A list representation of the path from the initial state to the goal, else None.
    """
    f_queue = [start]
    b_queue = [goal]
    f_explored = {start}
    b_explored = {goal}
    f_parent = {start: None}
    b_parent = {goal: None}

    while f_queue and b_queue:
        current_f = f_queue.pop()

        for neighbour in graph[current_f]:
            if neighbour in b_explored:
                return reconstruct_path(f_parent, b_parent, current_f, neighbour)
            if neighbour not in f_explored:
                f_explored.add(neighbour)
                f_queue.append(neighbour)
                f_parent[neighbour] = current_f

        current_b = b_queue.pop()
        
        for neighbour in graph[current_b]:
            if neighbour in f_explored:
                return reconstruct_path(f_parent, b_parent, current_b, neighbour)
            if neighbour not in b_explored:
                b_explored.add(neighbour)
                b_queue.append(neighbour)
                b_parent[neighbour] = current_b

    return "No path found"

def reconstruct_path(f_parent: dict, b_parent: dict, meeting_point_f: str, meeting_point_b: str):
    """Reconstructs the path from the initial state to the goal.

    Args:
        f_parent (dict): The pathway from the initial state to the meeting point.
        b_parent (dict): The pathway from the goal state to the meeting point.
        meeting_point_f (str): The node currently being explored.
        meeting_point_b (str): Its^ neighbour.

    Returns:
        List: The path from the initial state to the goal.
    """
    path_f = []
    current = meeting_point_f
    while current is not None:
        path_f.append(current)
        current = f_parent[current]
    path_f.reverse()

    path_b = []
    current = meeting_point_b
    while current is not None:
        path_b.append(current)
        current = b_parent[current]
    
    return path_f + path_b

def main():
    
    graph_1 = {
            'A': ['B', 'C', 'D'],
            'B': ['A', 'E', 'F'],
            'C': ['A', 'G'],
            'D': ['A', 'H', 'I', 'J'],
            'E': ['B', 'K', 'L'],
            'F': ['B', 'N'],
            'G': ['C'],
            'H': ['D'],
            'I': ['D', 'O'],
            'J': ['D'],
            'K': ['E'],
            'L': ['E', 'M'],
            'M': ['L'],
            'N': ['F'],
            'O': ['I']
        }

    print(bidirectional_search(graph_1, 'A', 'O'))

if __name__ == "__main__":
    main()

