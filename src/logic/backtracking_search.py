def backtrack(path: dict, current_state: str, goal_test: callable, depth=0):
    """Recursively traverse the search space, logging each step in detail."""
    indent = "  " * depth  # Indentation for better readability

    print(f"{indent}🔍 Exploring: {current_state}")
    possible_choices = path.get(current_state, [])  # Ensure safe lookup

    print(f"{indent}🔀 Possible choices: {possible_choices}")

    for choice in possible_choices:
        print(f"{indent}➡️ Checking choice: {choice}")

        if goal_test(choice):
            print(f"{indent}🎯 Goal '{choice}' found! Returning.")
            return choice

        if choice in path:
            print(f"{indent}↪️ Recursing into '{choice}'")
            result = backtrack(path, choice, goal_test, depth + 1)

            if result:
                return result
            else:
                print(f"{indent}⬅️ Backtracking from '{choice}'")

    print(f"{indent}❌ No valid path found from '{current_state}', backtracking...")
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