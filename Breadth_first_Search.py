from collections import deque

# Initialize the frontier, explored set, and expansions
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

def bfs(frontier, explored_set, pathways):
    if not frontier:
        print("There is no frontier to explore.")
        return

    while frontier[0] < 7:
        explored_set.append(frontier[0])
        frontier.append(pathways[frontier[0]])
        frontier.popleft()
        print("The following states have now been explored: ", end="")
        print(" ".join(map(str, explored_set)))
        frontier = deque([num for num in frontier if num not in explored_set])
        print("The frontier is now comprised of states ", end="")
        print(" ".join(map(str, frontier)), end="\n\n")

    print("Both rooms are now clean: the problem is resolved")

def main():
    bfs(room_states, states_visited, state_paths)

if __name__ == "__main__":
    main()
