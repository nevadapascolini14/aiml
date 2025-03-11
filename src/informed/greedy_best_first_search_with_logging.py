from queue import PriorityQueue

def greedy_best_first_search(graph: dict, start: str, heuristic: callable, goal: str):
    """Greedy Best-First Search for two-object graphs with detailed logging."""

    frontier = PriorityQueue()
    frontier.put((heuristic(start), start))  # (heuristic value, node)
    explored_set = set()
    
    print(f"\n🔍 Starting Greedy Best-First Search from '{start}'...\n")

    while not frontier.empty():
        heuristic_value, current_state = frontier.get()  # Get lowest heuristic value
        print(f"🛑 Expanding '{current_state}' with heuristic value {heuristic_value}")

        if current_state == goal:
            print(f"🎯 Goal '{goal}' reached!")
            return

        explored_set.add(current_state)

        # Get neighbors safely
        if current_state in graph:
            for neighbor, step_cost in graph[current_state].items():
                if neighbor not in explored_set:
                    neighbor_heuristic = heuristic(neighbor)
                    frontier.put((neighbor_heuristic, neighbor))
                    print(f"   ➕ Adding '{neighbor}' to frontier with heuristic {neighbor_heuristic}")

        print(f"   🔵 Frontier after expansion: {[item for item in frontier.queue]}\n")

    print("❌ Goal not found.")
    return None

def main():
    two_object_graph = {
        'A': {'B': 3, 'C': 3},
        'B': {'D': 2},
        'C': {'F': 3},
        'D': {'E': 4},
        'E': {'F': 1, 'G': 2},
        'F': {'G': 3},
        'G': {'H': 2}  # Goal state 'H'
    }

    def heur(node): 
        heuristic_values = {
            'A': 5, 'B': 6, 'C': 8, 'D': 4, 'E': 4, 
            'F': 5, 'G': 2, 'H': 0  # Goal state 'H' has heuristic 0
        }
        return heuristic_values.get(node, float('inf'))  # Default to large number if missing

    # Run GBFS
    greedy_best_first_search(two_object_graph, 'A', heur, 'H')

if __name__ == "__main__":
    main()
