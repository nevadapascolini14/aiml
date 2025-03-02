import pprint


def find_unit_clauses(formula):
    """Finds all unit clauses in the formula."""
    return {clause[0] for clause in formula if len(clause) == 1}


def unit_propagation(formula, assignment, unit_clauses):
    """Assigns values based on unit clauses and simplifies the formula."""
    print(f"Unit Propagation: Found unit clauses {unit_clauses}")
    for unit in unit_clauses:
        assignment[unit] = True
        formula = simplify(formula, unit)
        print(f"Assigned {unit} = True, Simplified Formula: {formula}")
    return formula, assignment


def pure_literal_elimination(formula, assignment, pure_literals):
    """Assigns values to pure literals and simplifies the formula."""
    print(f"Pure Literal Elimination: Found pure literals {pure_literals}")
    for literal in pure_literals:
        assignment[literal] = True
        formula = simplify(formula, literal)
        print(f"Assigned {literal} = True, Simplified Formula: {formula}")
    return formula, assignment


def simplify(formula, variable):
    """Removes satisfied clauses and eliminates negations of assigned variables."""
    new_formula = []
    for clause in formula:
        if variable in clause:
            continue  # Clause is satisfied, remove it
        new_clause = [x for x in clause if x != -variable]  # Remove negation
        new_formula.append(new_clause)
    return new_formula


def find_pure_literals(formula):
    """Finds pure literals in the formula (literals that appear only in one polarity)."""
    literals = get_all_literals(formula)
    pure_literals = {lit for lit in literals if -lit not in literals}
    return pure_literals


def get_all_literals(formula):
    """Extracts all unique literals from the formula."""
    literals = set()
    for clause in formula:
        literals.update(clause)
    return literals


def dpll(formula, assignment):
    """Recursive DPLL SAT Solver"""
    print("\n----------------------------------------")
    print(f"Starting DPLL with Formula: {formula}")
    print(f"Current Assignment: {assignment}")

    # Base cases
    if len(formula) == 0:
        print("✅ Formula is empty! SATISFIABLE with assignment:")
        pprint.pprint(assignment)
        return assignment

    for clause in formula:
        if len(clause) == 0:
            print("❌ Found an empty clause! UNSATISFIABLE")
            return "UNSATISFIABLE"

    # Unit propagation
    unit_clauses = find_unit_clauses(formula)
    if len(unit_clauses) != 0:
        formula, assignment = unit_propagation(formula, assignment, unit_clauses)
        return dpll(formula, assignment)

    # Pure literal elimination
    pure_literals = find_pure_literals(formula)
    if len(pure_literals) != 0:
        formula, assignment = pure_literal_elimination(
            formula, assignment, pure_literals
        )
        return dpll(formula, assignment)

    # Choose a variable using a heuristic (first literal in first clause)
    variable = abs(formula[0][0])
    print(f"Branching on variable {variable}")

    # Try assigning True
    new_assignment = assignment.copy()
    new_assignment[variable] = True
    print(f"Trying {variable} = True")
    result = dpll(simplify(formula, variable), new_assignment)
    if result != "UNSATISFIABLE":
        return result  # ✅ If SAT, return solution

    # Try assigning False if True failed
    new_assignment[variable] = False
    print(f"Trying {variable} = False")
    result = dpll(simplify(formula, -variable), new_assignment)

    return result if result != "UNSATISFIABLE" else "UNSATISFIABLE"


def main():
    print("\n=== Starting the SAT Solver ===")

    # Example CNF formula
    clauses = [[1, -3], [2, 3, -1], [-2, 3], [4], [-5]]
    model = {}  # Start with an empty assignment

    result = dpll(clauses, model)

    print("\n=== Final Result ===")
    if result == "UNSATISFIABLE":
        print("Formula is UNSATISFIABLE ❌")
    else:
        print("Formula is SATISFIABLE ✅")


if __name__ == "__main__":
    main()
