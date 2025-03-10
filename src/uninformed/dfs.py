from collections import deque

def dfs(start, routes, goal):
    frontier = deque([start])  # Stack for DFS
    explored_set = set()  # Keeps track of visited nodes
    parent_map = {start: None}  # Stores parent nodes for path reconstruction
    
    print("\n🔍 Starting DFS...\n")

    while frontier:
        print(f"🌟 Current Stack (Frontier): {list(frontier)}")  # Show stack state
        
        node = frontier.pop()  # LIFO: Get the last inserted node
        print(f"🛑 Popped from stack: {node}")

        if node == goal:  # Check if goal is found
            print("\n🎯 Goal found! Reconstructing path...\n")
            return reconstruct_path(parent_map, start, goal)

        # if node not in explored_set:
        #     explored_set.add(node)  # Mark node as visited
        #     print(f"✔ Marked '{node}' as visited.")

        # Add neighbors **in reverse order** to maintain correct DFS traversal
        for neighbor in reversed(routes.get(node, [])):  
            if neighbor not in explored_set and neighbor not in frontier:
                frontier.append(neighbor)
                parent_map[neighbor] = node
                print(f"➕ Added '{neighbor}' to stack (from '{node}').")
                print(f"📌 Updated parent map: {parent_map}")

    print("\n❌ Goal not found.")
    return None  # Return None if no path exists

def reconstruct_path(parent_map, start, goal):
    """Backtracks from goal to start using parent_map to reconstruct the path."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent_map[current]
    path.reverse()  # Reverse to get path from start to goal

    print(f"🔗 Path found: {' -> '.join(path)}\n")
    return path  # Now correctly returns the path

# Example Tree Structure as an adjacency list
tree = {
    'A': ['B', 'C'],
    'B': ['D'],
    'D': ['F'],
    'C': ['E'],
    'E': ['G'],
    'G': ['H']  # Goal
}

# Run DFS to find 'H'
solution = dfs('A', tree, 'H')
print("\n✅ Final Path Found:", solution if solution else "❌ No path found.")

    
