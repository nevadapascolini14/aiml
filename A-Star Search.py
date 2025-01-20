from queue import PriorityQueue

begin = 'A'
end = 'H'

avoid_obj_graph = {
    'A': {'B': 3, 'C': 3},
    'B': {'D': 2},
    'C': {'F': 3},
    'D': {'E': 4},
    'E': {'F': 1, 'G': 2},
    'F': {'G': 3},
    'G': {'H': 2} 
    }

heur = {
    'A': 5,
    'B': 6,
    'C': 8,
    'D': 4,
    'E': 4,
    'F': 5,
    'G': 2,
    'H': 0
}

def A_Star_Search (graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start)) # priority queues define position and value
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()[1] # 1 because each elememnt of tuple counts as an element

        if current == goal:
            return reconstruct_path(came_from, start, goal), cost_so_far[goal]

        for next in graph[current]: # the value (dict) of current
            new_cost = cost_so_far[current] + graph[current][next] # iterates ovver dict pairs
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heur.get(next)
                frontier.put((priority, next))
                came_from[next] = current

    return None, None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def main():
    path, cost = A_Star_Search(avoid_obj_graph, 'A', 'H')
    if path:
        print(f"Path: {path}")
        print(f"Total Cost: {cost}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()

