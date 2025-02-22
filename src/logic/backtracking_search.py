def backtrack(path: dict, current_state: str, goal_test: callable):
    """Recursively traverse the search space, returning the goal if condition is found.

    Args:
        path (dict): a dictionary of reachable nodes from each key node
        current_state (str): The current node to be checked.
        goal_test (callable): A function that checks if a state is a goal state

    Returns:
        str or None: a string, signifying the goal, supposing there is one, else None
    """
    possible_choices = path[current_state]
    print(f"Current state: {current_state}")
    print(f"possible choices: {possible_choices}", end="\n\n")   

    for choice in possible_choices:
        if goal_test(choice):
            return choice
    
        if choice in path:
            result = backtrack(path, choice, goal_test)
            if result:
                return result
            
    return None

def backward_chain(clauses: list, assignment: set):
    """Uses a backtracking approach to check whether the given list of CNF clauses is satisfiable.

    Args:
        clauses (list): A list of CNF clauses to be tested for satisfiability.
        assignment (set): The model of assigned literals to be tested.

    Returns:
        set or False: A set of literals satisfying the clauses, if one exists, else None
    """
    if all(is_clause_satisfied(clause, assignment) for clause in clauses):
        return assignment
    
    unassigned = {abs(lit) for clause in clauses for lit in clause} - {abs(lit) for lit in assignment}
    if not unassigned:
        return False  
    
    literal = next(iter(unassigned))  
    
    if (result := backward_chain(clauses, assignment.copy() | {literal})):
        return result

    if (result := backward_chain(clauses, assignment.copy() | {-literal})):
        return result

    return False  

def is_clause_satisfied(clause: list, assignment: set):
    """Checks whether a CNF clause is satisfied by a given set of literals

    Args:
        clause (list): A CNF clause to be tested for satisfiability.
        assignment (set): The model of assigned literals to be tested.

    Returns:
        boolean: True if the assignment satisfies the clause, else False
    """
    return any(literal in assignment for literal in clause)

def main():
    
    clauses_1 = [[1, 2, 3],
           [-1, 2, 3],
           [-1, -2, -3],
           [-2, 3],
           [2, -3]]
    
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
    
    satisfying_assignment = backward_chain(clauses_1, set())

    if satisfying_assignment:
        print("SATISFIABLE with assignment:", satisfying_assignment)
    else:
        print("UNSATISFIABLE")

    """result = backtrack(path_1, start, goal_test_1)
    
    if result:
        print(f"Goal: {result}")"""

if __name__ == "__main__":
    main()