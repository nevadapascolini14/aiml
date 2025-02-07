path_1 = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I', 'J'],
    'E': ['K', 'L'],
    'F': ['N'],
    'I': ['O'],
    'L': ['M']
}

def goal_test_1(node: str):
    return node == 'O'

start = 'A'

def backtrack(path: dict, current_state: int, goal_test: callable):
    possible_choices = path[current_state]
    print(f"Current state: ", current_state)
    print(f"possible choices: ", possible_choices, end="\n\n")   

    for choice in possible_choices:
        if goal_test(choice):
            return choice
    
        if choice in path:
            result = backtrack(path, choice, goal_test)
            if result:
                return result
            
    return None

def main():
    
    result = backtrack(path_1, start, goal_test_1)
    if result:
        print(f"Goal: {result}")

if __name__ == "__main__":
    main()