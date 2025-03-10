import time

def depth_limited_search(problem, node, goal, depth_limit):
    """Performs Depth-Limited Search up to a given depth limit with detailed logging."""
    frontier = [(node, 0, [node])]  # Stack (LIFO) of (node, depth, path)
    result = None  # Stores whether we hit the depth limit

    print(f"\nStarting Depth-Limited Search with depth limit: {depth_limit}")
    
    while frontier:
        current_node, depth, path = frontier.pop()  # Pop from stack (LIFO)
        
        print(f"  - Exploring Node: {current_node}, Depth: {depth}, Path so far: {path}")

        if current_node == goal:
            print(f"🎯 Goal found at Node {current_node}! Returning path: {path}")
            return path  # Goal found, return the path

        if depth >= depth_limit:
            print(f"  ⏳ Reached depth limit at Node {current_node}, marking as cutoff.")
            result = "cutoff"  # Indicate we hit depth limit
            continue

        # Expand children and push onto stack
        for child in reversed(problem.get(current_node, [])):  # Reverse to maintain left-to-right order
            print(f"    ↳ Adding Child {child} to frontier at depth {depth + 1}")
            frontier.append((child, depth + 1, path + [child]))

    print(f"  ❌ No solution found at depth limit {depth_limit}, returning: {result}")
    return result  # Return "cutoff" if depth limit was reached, else return failure


def iterative_deepening_search(problem, start, goal):
    """Performs IDDFS by calling Depth-Limited Search iteratively with increasing depth."""
    depth = 0
    while True:
        print(f"\n🌟 Iteration with Depth Limit: {depth}")
        result = depth_limited_search(problem, start, goal, depth)
        if result != "cutoff":  # If result is a path or failure (None), return it
            print(f"✅ Solution found at depth {depth}: {result}")
            return result
        depth += 1  # Increase depth limit
        time.sleep(0.5)  # Pause for readability


# Example Tree Structure as an adjacency list
tree = {
    'A': ['B', 'C'],
    'B': ['D'],
    'D': ['F'],
    'C': ['E'],
    'E': ['G'],
    'G': ['H']  # Goal
}

# Run IDDFS to find 'H'
solution = iterative_deepening_search(tree, 'A', 'H')
print("\nFinal Path Found:", solution)
