import heapq

def reconstruct_path(reached_F, reached_B, meeting_point):
    """Reconstructs the full path from start to goal via the meeting point."""
    path_F, path_B = [], []
    
    # Build path from start to meeting point
    node = meeting_point
    while node is not None:
        path_F.append(node)
        node = reached_F[node]
    path_F.reverse()

    # Build path from meeting point to goal
    node = reached_B[meeting_point]
    while node is not None:
        path_B.append(node)
        node = reached_B[node]

    return path_F + path_B  # Merge forward and backward paths

def proceed(direction, frontier, graph, reached, reached_other):
    """Expands the lowest-cost node in the given frontier and checks for intersection."""
    cost, node = heapq.heappop(frontier)  # Get the lowest-cost node
    
    direction_text = "FORWARD" if direction == "F" else "BACKWARD"
    print(f"\n🔍 {direction_text} EXPANSION: Expanding node '{node}' with cost {cost}")

    for neighbor, edge_cost in graph.get(node, []):
        new_cost = cost + edge_cost  # Compute updated cost
        
        if neighbor not in reached or new_cost < reached[neighbor][1]:  # If not visited OR found cheaper path
            reached[neighbor] = (node, new_cost)  # Store parent and cost
            heapq.heappush(frontier, (new_cost, neighbor))  # Push to priority queue
            print(f"   ➕ Adding '{neighbor}' to {direction_text} frontier with cost {new_cost}")

        if neighbor in reached_other:  # If found by the other search
            print(f"   🎯 Meeting point found at '{neighbor}'!")
            return neighbor  # Meeting point found

    print(f"   ✅ {direction_text} frontier after expansion: {[(cost, node) for cost, node in frontier]}")
    return None  # No meeting point yet

def bibf(start: str, graph: dict, goal: str):
    """Bidirectional Best-First Search (BiBF-Search)"""
    
    # Priority queues for forward and backward search
    frontier_F = [(0, start)]  # (cost, node)
    frontier_B = [(0, goal)]   # (cost, node)
    heapq.heapify(frontier_F)
    heapq.heapify(frontier_B)
    
    # Reached nodes (store parent and cost)
    reached_F = {start: (None, 0)}  # (parent, cost)
    reached_B = {goal: (None, 0)}  # (parent, cost)

    print(f"\n🔍 Starting BiBF-Search from '{start}' to '{goal}'...\n")

    while frontier_F and frontier_B:
        print(f"\n🌟 Current FRONTIER STATES:")
        print(f"   🔵 Forward frontier: {[(cost, node) for cost, node in frontier_F]}")
        print(f"   🔴 Backward frontier: {[(cost, node) for cost, node in frontier_B]}")

        # Expand the frontier with the lower priority value
        if frontier_F[0][0] < frontier_B[0][0]:  
            meeting_point = proceed("F", frontier_F, graph, reached_F, reached_B)
        else:
            meeting_point = proceed("B", frontier_B, graph, reached_B, reached_F)

        # If the searches meet, reconstruct the path
        if meeting_point:
            print(f"\n🎯 FINAL MEETING POINT FOUND: '{meeting_point}'")
            path = reconstruct_path({k: v[0] for k, v in reached_F.items()}, {k: v[0] for k, v in reached_B.items()}, meeting_point)
            print(f"\n✅ FINAL PATH FOUND: {' -> '.join(path)}\n")
            return path

    print("\n❌ No solution found.")
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

# Run BiBF-Search
bibf("A", graph, "H")
