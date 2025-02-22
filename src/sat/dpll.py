def find_pure_symbol(clauses: list, symbols: set, model: list):
    """Identifies literals that appear exclusively in their positive or negative forms

    Args:
    clauses (list): a list of propositional logic clauses, written in CNF
    symbols (set): the set of propositions appearing in Clauses
    model (list): the configuration of positive and negative propositions to be examined

    Returns:
    A proposition that occurs exclusively in positive or negative form, or one.
    """
    for prop in symbols: 
        if prop in model or -prop in model:
            continue

        i = None
        pure = True

        for clause in clauses: 
            for item in clause:
                if abs(item) == prop:
                    if i is None:
                        i = item       
                    elif item != i:
                        pure = False

        if pure and i is not None:
            return i    
        
    return None

def find_unit_clause(clauses: list, model: list):
    """infers truth status of a proposition by simplification

    Args:
    clauses (list): a list of propositional logic clauses, written in CNF
    model (list): the configuration of positive and negative propositions to be examined

    Returns:
    an inferred proposition, or None.
    """
    for clause in clauses:
        new_clause = []
        for item in clause:
            if -item not in model and item not in model:
                new_clause.append(item)
        
        if len(new_clause) == 1:
                    return new_clause[0]
    return None

def dpll(clauses: list, symbols: set, model: list):
    """
    Implements the DPLL algorithm to check satisfiability of set of CNF clauses.

    Args:
    clauses (list): a list of propositional logic clauses, written in CNF
    symbols (set): the set of propositions appearing in clauses
    model (list): the configuration of positive and negative propositions to be examined

    Returns:
    a satisfying assignment (model) if one exists, otherwise False.
    """
    satisfied = True
    for clause in clauses:
        if not any(lit in model for lit in clause):  # Clause is not satisfied
            satisfied = False
            break
    
    if satisfied:
        return model  
    
    for clause in clauses:
        if all(-lit in model for lit in clause):  # All literals in clause are false
            return False  
    
    p = find_pure_symbol(clauses, symbols, model)
    if p is not None:
        return dpll(clauses, symbols - {abs(p)}, model + [p])
    
    p = find_unit_clause(clauses, model)
    if p is not None:
        return dpll(clauses, symbols - {abs(p)}, model + [p])

    # Choose an arbitrary symbol 
    p = next(iter(symbols))
    rest = symbols - {p}

    # Try both assignments (p=True and p=False)
    model_true = dpll(clauses, rest, model + [p])
    if model_true:
        return model_true  

    model_false = dpll(clauses, rest, model + [-p])
    if model_false:
        return model_false  

    return False  

def main():
    
    sample_symbols = {1, 2, 3}
    sample_list = [
                  [1, 2, 3],
                  [-1, 2, 3],
                  [-1, -2, -3],
                  [-2, 3],
                  [2, -3]
                  ]
    sample_model = []

    print(dpll(sample_list, sample_symbols, sample_model))

if __name__ == "__main__":
    main()

