from collections import deque

def depth_limited_search(routes: dict, start: str, goal: str, depthlim: int):
    """Performs Depth-Limited Search (DLS) up to depthlim with enhanced depth logging."""
    
    if start == goal:
        print(f"🎯 Goal '{goal}' found immediately at depth 0!")
        return True

    frontier = deque([(start, 0)])  # (node, depth)

    print(f"\n🔍 Starting Depth-Limited Search from '{start}' to '{goal}' with depth limit {depthlim}...\n")

    while frontier:
        node, depth = frontier.pop()  # Pop node and depth from stack
        print(f"🛑 Popped node '{node}' from stack (Depth: {depth})")

        if node == goal:
            print(f"🎯 Goal '{goal}' found at depth {depth}!")
            return True

        if depth < depthlim:  # Expand only if within depth limit
            print(f"   🔽 Expanding node '{node}' (Depth {depth})...")
            children = routes.get(node, [])

            if children:
                print(f"   ➕ Adding children {children} at depth {depth+1} to stack")
                for child in children:
                    frontier.append((child, depth + 1))
            else:
                print(f"   ⚠️ '{node}' has no children. Skipping expansion.")

        else:
            print(f"   ❌ Reached depth limit at '{node}' (Depth: {depth}). Stopping expansion.")

        print(f"   🔵 Current Frontier: {list(frontier)}\n")

    print(f"❌ Goal '{goal}' not found within depth limit {depthlim}.")
    return False  # Goal not found

# Example Graph
path_1 = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": ["H", "I", "J"],
    "E": ["K", "L"],
    "F": ["N"],
    "I": ["O"],
    "L": ["M"],  # Goal is here
}

# Run DLS
depth_limited_search(path_1, "A", "M", 4)
