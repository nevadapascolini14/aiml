'''
Make a FIFO (first-in-first-out) queue to store the frontier. This doesn't have to be efficient, you can use a very simple Java type such as an ArrayList here. The queue is initialised with one element (the initial state, 1). The ArrayList methods add, size, get and remove are relevant here, and you can revise ArrayLists from the Algorithms & Data Structures module. 
Set up another data structure to store the explored set. Again this does not need to be efficient, you could use an ArrayList.
Write the main loop, as shown in the pseudocode. Each iteration of the main loop takes one node from the frontier, adds it to the explored set and then expands it. 
To expand a node, you will need to look up neighbouring states in some way (for example from an array). For example, the neighbours of state 4 are 3, 4, and 8. 
'''

from collections import deque

def bfs(start: str, routes: dict, goal: str):
    fifo_frontier = deque([start])  # Queue for BFS
    explored_set = set()  # Set for visited nodes
    parent_map = {start: None}  # Track path to reconstruct it

    print(f"\n🔍 Starting BFS from '{start}' to reach '{goal}'...\n")

    while fifo_frontier:
        print(f"🌟 Current Frontier: {list(fifo_frontier)}")  # Show current queue
        
        key = fifo_frontier.popleft()  # Get the first node from the queue
        print(f"🛑 Dequeued: {key}")

        if key == goal:  # Goal check
            print(f"\n🎯 Goal '{goal}' found! Reconstructing path...\n")
            return reconstruct_path(parent_map, start, goal)

        # if key not in explored_set:
        #     explored_set.add(key)  # Mark node as explored
        #     print(f"✔ Marked '{key}' as visited.")

        for neighbor in routes[key]:
            if neighbor not in explored_set and neighbor not in fifo_frontier:
                fifo_frontier.append(neighbor)
                parent_map[neighbor] = key  # Store parent for path reconstruction
                print(f"➕ Added '{neighbor}' to queue (from '{key}').")

    print("\n❌ Goal not found.")
    return None  # Return None if no path exists

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

# Example usage
def main():
    routes = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["A","B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }
    
    result = bfs("A", routes, "E")  
    print(f"\n✅ Final result: {result}" if result else "❌ No path found.")

main()
