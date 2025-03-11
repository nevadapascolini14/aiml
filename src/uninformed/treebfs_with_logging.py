from collections import deque

def tree_bfs(start: str, tree: dict, goal: str):
    """Breadth-First Search for a Tree (No cycles, no duplicate parents)."""
    
    fifo_frontier = deque([start])  # BFS Queue
    parent_map = {start: None}  # Tracks the parent of each node

    print(f"\n🌲 Starting BFS for a TREE from '{start}' to '{goal}'...\n")

    while fifo_frontier:
        print(f"🌟 Current Frontier: {list(fifo_frontier)}")  # Show current queue
        
        node = fifo_frontier.popleft()  # Get the first node from the queue
        print(f"🛑 Dequeued: {node}")

        if node == goal:  # Goal check
            print(f"\n🎯 Goal '{goal}' found! Reconstructing path...\n")
            return reconstruct_path(parent_map, start, goal)

        for child in tree.get(node, []):  # Expand child nodes
            if child not in parent_map:  # Ensure only one parent (tree property)
                fifo_frontier.append(child)
                parent_map[child] = node  # Track parent for path reconstruction
                print(f"➕ Added '{child}' to queue (from '{node}').")

    print("\n❌ Goal not found.")
    return None  # Return None if no path exists

# Helper function to reconstruct path
def reconstruct_path(parent_map, start, goal):
    """Backtrack from goal to start using parent_map to reconstruct path."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent_map[current]
    path.reverse()  # Reverse to get path from start to goal

    print(f"🔗 Path found: {' -> '.join(path)}\n")
    return path

# Example usage for a TREE (no cycles)
def main():
    tree_structure = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["G"],
        "E": ["H", "I"],
        "F": ["J"],
        "G": [],
        "H": [],
        "I": [],
        "J": []
    }
    
    result = tree_bfs("A", tree_structure, "I")  
    print(f"\n✅ Final result: {result}" if result else "❌ No path found.")

main()
