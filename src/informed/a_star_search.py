from queue import PriorityQueue

def A_Star_Search(graph: dict, start: str, heuristic: callable):
    """_summary_

    Args:
        graph (dict): a dictionary of reachable nodes from each key node
        start (str): the name of the starting node
        heuristic (callable): the distance to the goal

    Returns:
        A dict representing the optimal path to the goal, else None
    """
    
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1]

        if heuristic(current) == 0:
            return reconstruct_path(came_from, start, current), cost_so_far[current]

        for next in graph[current]:
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                frontier.put((priority, next))
                came_from[next] = current

    return None, None

def reconstruct_path(came_from: dict, start: str, goal: str):
    """Reconstructs the optimal path from the starting vertex to the goal.

    Args:
        came_from (dict): a dict representing paths between vertexes
        start (str): The starting vertex
        goal (str): The goal vertex

    Returns:
        list: the optimal path from the starting vertex to the goal.
    """
    
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def main():

    two_object_graph = {
        'A': {'B': 3, 'C': 3},
        'B': {'D': 2},
        'C': {'F': 3},
        'D': {'E': 4},
        'E': {'F': 1, 'G': 2},
        'F': {'G': 3},
        'G': {'H': 2} 
        }

    def heur (node): 
        straight_line_distance = {
        'A': 5,
        'B': 6,
        'C': 8,
        'D': 4,
        'E': 4,
        'F': 5,
        'G': 2,
        'H': 0
    }
        return straight_line_distance.get(node)

    crates_graph = {
        'A': {'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'A': 1},
        'B': {'C': 1, 'H': 1, 'B': 1},
        'C': {'B': 1, 'I': 1, 'C': 1},
        'D': {'E': 1, 'J': 1, 'D': 1},
        'E': {'D': 1, 'K': 1, 'E': 1},
        'F': {'G': 1, 'L': 1, 'F': 1},
        'G': {'F': 1, 'M': 1, 'G': 1},
        'H': {'N': 1},
        'I': {'O': 1},
        'J': {'P': 1},
        'K': {'Q': 1},
        'L': {'R': 1},
        'M': {'S': 1}
    }

    stack_height = {
        'A': 1,
        'B': 2,
        'C': 2,
        'D': 2,
        'E': 2,
        'F': 2,
        'G': 2,
        'H': 3,
        'I': 3,
        'J': 3,
        'K': 3,
        'L': 3,
        'M': 3,
        'N': 4,
        'O': 4,
        'P': 4,
        'Q': 4,
        'R': 4,
        'S': 4,
    }

    def heur_2(height):
        result = stack_height.get(height)
        if result is None:
            print(f"Missing height for node: {height}")
        return 4 - result if result is not None else 4
    
    path, cost = A_Star_Search(crates_graph, 'A', heur_2)
    if path:
        print(f"Path: {path}")
        print(f"Total Cost: {cost}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

