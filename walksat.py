import random

def walksat(clauses: list, p: float, max_flips: int, model: list):
    """Attempts to determine a satifyng model for a set of CNF clauses.

    Args:
        clauses (list): A list of CNF clauses
        p (float): Probility of flipping a random literal or 'optimal' literal.
        max_flips (int): Maximum number of iterations of the algorithm.
        model (list): The configuration of positive and negative propositions to be examined.

    Returns:
        List: A satisfying model, else None.
    """
    
    
    for i in range(max_flips):
        satisfied = True
        false_clauses = []

        for clause in clauses:
            if not any(lit in model for lit in clause):  # Clause is not satisfied
                satisfied = False
                false_clauses.append(clause)
        
        if satisfied:
            print(f"Satisfying model found: {model}")
            return model  

        rand_clause = random.choice(false_clauses)
        
        if random.random() < p:
            rand_lit = random.choice(list(rand_clause))

            for j, item in enumerate(model):
                if item == rand_lit or item == -rand_lit:
                    model[j] = -item
            print('a', model)
        else:
            satisfied_clauses = {}

            for lit in rand_clause:
                count = sum(1 for clause in clauses if -lit in clause)
                satisfied_clauses[lit] = count

            max_key = max(satisfied_clauses, key = satisfied_clauses.get)
                
            for j, item in enumerate(model):
                if item == max_key or item == -max_key:
                    model[j] = -item
            print('b', model)
                           
def main():

    clauses_1 = [
                  {1, 2, 3},
                  {-1, 2, 3},
                  {-1, -2, -3},
                  {-2, 3},
                  {2, -3}
                  ]

    walksat(clauses_1, 0.5, 100, [1, 2, 3])

if __name__ == "__main__":
    main()