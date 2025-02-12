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

clauses_1 = [[1, 2, 3],
           [-1, 2, 3],
           [-1, -2, -3],
           [-2, 3],
           [2, -3]]

def is_clause_satisfied(clause, assignment):
    """Checks if a given clause is satisfied by the current assignment."""
    return any(literal in assignment for literal in clause)

def backward_chain(clauses, assignment=set()):
    """
    Checks if the given set of CNF clauses is satisfiable.
    Uses a backtracking approach to find a valid truth assignment.
    """
    if all(is_clause_satisfied(clause, assignment) for clause in clauses):
        return assignment
    
    # Create dict of unassigned clauses
    unassigned = {abs(lit) for clause in clauses for lit in clause} - {abs(lit) for lit in assignment}
    if not unassigned:
        return False  
    
    literal = next(iter(unassigned))  
    
    # Try assigning literal as True
    if (result := backward_chain(clauses, assignment | {literal})):
        return result

    # Try assigning literal as False 
    if (result := backward_chain(clauses, assignment | {-literal})):
        return result

    return False  # If neither assignment works, the set of clauses is unsatisfiable

def main():
    
    satisfying_assignment = backward_chain(clauses_1)

    if satisfying_assignment:
        print("SATISFIABLE with assignment:", satisfying_assignment)
    else:
        print("UNSATISFIABLE")

    """result = backtrack(path_1, start, goal_test_1)
    if result:
        print(f"Goal: {result}")"""

if __name__ == "__main__":
    main()