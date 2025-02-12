from collections import deque

route_states = deque(['A'])
states_visited = []

state_paths = {
    'A': [5, 'B', 'C'],
    'B': [6, 'A', 'D'],
    'C': [8, 'A', 'F'],
    'D': [4, 'B', 'E'],
    'E': [4, 'D', 'F', 'G'],
    'F': [5, 'E', 'G'],
    'G': [2, 'E', 'F', 'H'],
    'H': [0, 'G']
}

def goal_test_1(heur: int):
    return heur == 0  # Explicitly return False when the goal is not met

def greedy_best_first_search(frontier, explored_set, pathways, goal_test: callable):
    if not frontier:
        print("There is no frontier to explore.")
        return

    while frontier:
        current_state = frontier.popleft()  # Pop leftmost (lowest heuristic)
        
        if goal_test(pathways[current_state][0]):  # Check if goal is met
            print(f"Goal reached at {current_state}")
            return

        explored_set.append(current_state)

        # Add neighbors to frontier, avoiding revisiting explored states
        neighbors = pathways[current_state][1:]
        for neighbor in neighbors:
            if neighbor not in explored_set and neighbor not in frontier:
                frontier.append(neighbor)

        # Select the next state with the lowest heuristic
        if frontier:
            min_key = min(frontier, key=lambda state: pathways[state][0])
            frontier = deque([min_key])  # Reset the frontier to contain only the best state
        
        print("We have now arrived at state", min_key)

def main():
    greedy_best_first_search(route_states, states_visited, state_paths, goal_test_1)

if __name__ == "__main__":
    main()

            
