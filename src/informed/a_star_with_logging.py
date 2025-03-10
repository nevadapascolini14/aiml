from queue import PriorityQueue

def reconstruct_path

def a_star_search(graph, start, heuristic):
    frontier = PriorityQueue()
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    print(came_from)
    print(cost_so_far)
    
    while not frontier.empty():
        current = frontier.get()[0]
        
        if heuristic(current) == 0:
            return recons

a_star_search("d","d","d")

    
