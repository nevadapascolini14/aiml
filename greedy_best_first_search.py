from queue import PriorityQueue
from collections import deque

def greedy_best_first_search(start: str, pathways: dict, goal_test: callable):
    """Searches for a goal state by always exploring the reachable state closest to the goal.

    Args:
        start (str): The initial state
        pathways (dict): A dictionary representing pathways between states and heuristic values
        goal_test (callable): A function that checks if a state is a goal state
    """
    frontier = PriorityQueue()
    frontier.put((pathways[start][0], start))  

    explored_set = set()

    while not frontier.empty():

        _, current_state = frontier.get()  

        if goal_test(pathways[current_state][0]):  
            print(f"Goal reached at {current_state}")
            return

        explored_set.add(current_state)
        neighbors = pathways[current_state][1:]

        for neighbor in neighbors:
            if neighbor not in explored_set:
                frontier.put((pathways[neighbor][0], neighbor))  

        if not frontier.empty():
            current_state = frontier.queue[0][1]  

        print("We have now arrived at state", current_state)

def main():

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
        return heur == 0  
    
    greedy_best_first_search('A', state_paths, goal_test_1)

if __name__ == "__main__":
    main()

            
