from queue import PriorityQueue

def A_Star_Search(graph: dict, start: str, heuristic: callable):
    """A* Search Algorithm with detailed cost breakdown logging."""

    frontier = PriorityQueue()
    frontier.put((0, start))  # (Priority f(n), Node)
    came_from = {}  # Tracks the path
    cost_so_far = {}  # Tracks cost from start node (g(n))
    came_from[start] = None
    cost_so_far[start] = 0

    print(f"\n🔍 Starting A* Search from '{start}'...\n")

    while not frontier.empty():
        current_priority, current = frontier.get()  # Get the lowest f(n)
        print(f"🛑 Popped node '{current}' from frontier (Priority f(n): {current_priority}, Cost g(n): {cost_so_far[current]})")

        if heuristic(current) == 0:  # Goal condition
            print(f"🎯 Goal '{current}' reached with total cost {cost_so_far[current]}!\n")
            path = reconstruct_path(came_from, start, current)
            print(f"✅ Optimal Path Found: {path}")
            return path, cost_so_far[current]

        print(f"   🔍 Expanding node '{current}'...")

        for neighbor, step_cost in graph[current].items():
            previous_cost = cost_so_far[current]  # g(n) of current node
            new_cost = previous_cost + step_cost  # g(n) + step_cost
            heuristic_cost = heuristic(neighbor)  # h(n)
            total_priority = new_cost + heuristic_cost  # f(n) = g(n) + h(n)

            print(f"   ↳ Considering neighbor '{neighbor}'...")
            print(f"     - Previous cost g(n): {previous_cost}")
            print(f"     - Step cost: {step_cost}")
            print(f"     - New total cost g(n): {new_cost}")
            print(f"     - Heuristic cost h(n): {heuristic_cost}")
            print(f"     - Total priority f(n): {total_priority}")

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                frontier.put((total_priority, neighbor))
                came_from[neighbor] = current
                print(f"   ➕ Adding '{neighbor}' to frontier with cost g(n)={new_cost}, priority f(n)={total_priority}")

        print(f"   🔵 Frontier after expansion: {[item for item in frontier.queue]}\n")

    print("❌ No path found.")
    return None, None

def reconstruct_path(came_from: dict, start: str, goal: str):
    """Reconstructs the optimal path from the starting vertex to the goal."""
    
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

    def heur(node): 
        straight_line_distance = {
            'A': 5, 'B': 6, 'C': 8, 'D': 4, 'E': 4, 
            'F': 5, 'G': 2, 'H': 0  # Goal node 'H' has heuristic 0
        }
        return straight_line_distance.get(node, float('inf'))  # Default to large number if missing

    # Run A* Search with logging
    path, cost = A_Star_Search(two_object_graph, 'A', heur)
    
    if path:
        print(f"\n🚀 Final Path: {path}")
        print(f"💰 Total Cost: {cost}")
    else:
        print("❌ No path found.")

if __name__ == "__main__":
    main()
