import heapq

def ucs(start: str, routes: dict, goal: str):
    """Uniform-Cost Search (UCS) to find the least-cost path."""
    frontier = [(0, start)]  # Priority queue (cost, node)
    explored_set = {}  # Dictionary to store best-known cost to each node

    while frontier:
        current_cost, node = heapq.heappop(frontier)  # Extract (cost, node)
        print(f"🔍 Exploring node '{node}' with current cost {current_cost}")

        if node == goal:
            print(f"🎯 Goal '{goal}' found with total cost {current_cost}!")
            return current_cost  # Return the cost to reach the goal

        # If we find a cheaper way to reach the node, update
        if node not in explored_set or current_cost < explored_set[node]:
            explored_set[node] = current_cost  # Store the best known cost

            for neighbor, step_cost in routes.get(node, []):  # Expand neighbors
                new_cost = current_cost + step_cost  # Calculate total cost
                
                if neighbor == goal:
                    print(f"🎯 Goal '{goal}' found with total cost {new_cost}!")
                    return new_cost  # Stop immediately when goal is added

                if neighbor not in explored_set or new_cost < explored_set[neighbor]:
                    explored_set[neighbor] = new_cost
                    heapq.heappush(frontier, (new_cost, neighbor))
                    print(f"   ➕ Adding '{neighbor}' to frontier with cost {new_cost}")

        print(f"   🔵 Frontier after expansion: {frontier}")

    print("❌ Goal not found")
    return None

# Example graph (Adjacency List with Costs)
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 7), ('E', 3)],
    'C': [('A', 4), ('F', 5)],
    'D': [('B', 7), ('G', 1)],
    'E': [('B', 3), ('G', 6)],
    'F': [('C', 5), ('G', 2)],
    'G': [('D', 1), ('E', 6), ('F', 2), ('H', 3)],
    'H': [('G', 3)]
}

# Run UCS
ucs("A", graph, "G")
