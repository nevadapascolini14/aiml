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

def greedy_best_first_search(frontier, explored_set, pathways):
    if not frontier:
        print("There is no frontier to explore.")
        return

    while state_paths[frontier[0]][0] !=0:
        explored_set.append(frontier[0])
        frontier.extend(state_paths[frontier[0]][1:])
        frontier = deque([cha for cha in frontier if cha not in explored_set])
        min_value = float('inf')
        min_key = None

        for value in frontier:
            if state_paths[value][0] < min_value:
                min_value = state_paths[value][0]
                min_key = value
                frontier = deque([min_key])
        print("We have now arrived at state", min_key)

def main():
    greedy_best_first_search(route_states, states_visited, state_paths)

if __name__ == "__main__":
    main()
            
