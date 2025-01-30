from collections import deque
from typing import Any, Callable, Dict, List, Set

room_states = deque([1])
states_visited = []
state_paths = {
    1: [1, 2, 3],
    2: [1, 2, 6],
    3: [3, 4, 3],
    4: [3, 4, 8],
    5: [5, 6, 7],
    6: [5, 6, 6],
    7: [7, 8, 7],
    8: [7, 8, 8],
}

def end (state):
    if state > 6:
        return True

def bfs(frontier: deque, explored_set: list, pathways: dict, goal: Callable[[int], bool]):
    """Performs a breadth-first search
    
    Args:
    frontier: The queue of states to explore (deque).
    explored_set: The list of explored states (list).
    pathways: A dictionary representing connections between states (dict).
    goal: A function that checks if a state is a goal state (Callable).
    """
    resolved = False

    while not resolved:
        explored_set.append(frontier[0])
        
        for value in pathways[frontier[0]]:
            if value not in explored_set:
                frontier.append(value)

        frontier.popleft()
        resolved = goal(frontier[0])

        print(f"The following states have now been explored: ")
        print(" ".join(map(str, explored_set)), end="\n\n")
        print(f"The new frontier is comprised of states ")
        print(" ".join(map(str, frontier)), end="\n\n\n")

    print("Both rooms are now clean: the problem is resolved")

def main():
    bfs(room_states, states_visited, state_paths, end)

if __name__ == "__main__":
    main()
