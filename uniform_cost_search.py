from queue import PriorityQueue

graph_1 = {'A': [(1, 'B'), (2, 'C'), (3, 'D')],
           'B': [(4, 'E'), (5, 'F')],
           'C': [(6, 'G')],
           'D': [(7, 'H'), (8, 'I'), (9, 'J')],
           'E': [(8, 'K'), (7, 'L')],
           'F': [(6, 'N')],
           'G': [(5, 'O')],
           'I': [(4, 'O')],
           'L': [(3, 'M')],
           'M': [(2, 'O')]
           }

start_1 = 'A'

def goal_test_1(node: str):
    return node == 'O'

def get_unexplored(p_queue: PriorityQueue, explored):
    while not p_queue.empty():
        entry = p_queue.get()
        if len(entry) == 2: 
            priority, node = entry
            if node not in explored:
                return priority, node
    return None

def ucs(graph: dict, start: str, goal: callable):
    queue = PriorityQueue()
    explored_set = set()
    cost_so_far = {}
    parent_map = {}  
    queue.put((0, start))
    parent_map[start] = None  

    while not queue.empty():
        result = get_unexplored(queue, explored_set)
        if result is None:
            break

        priority, node = result

        if goal(node):
            print(f"You have reached the goal: {node}")
            
            path = []
            while node is not None:
                path.append(node)
                node = parent_map[node]
            path.reverse()  

            print("Path:", " -> ".join(path))
            return  
        
        explored_set.add(node)
        cost_so_far[node] = priority

        for value in graph.get(node, []):  
            new_cost = value[0] + priority
            neighbor = value[1]

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent_map[neighbor] = node  
                queue.put((new_cost, neighbor)) 
        
        print(f"Path costs: ", cost_so_far, "\n")
        print(f"Already explored: ", explored_set, "\n\n")

    return None

def main():
    
    ucs(graph_1, start_1, goal_test_1)

if __name__ == "__main__":
    main()