def tt_entails(kb: list, a: list, symbols: list):
    """Determines entailment: whether sentence 'a' is true in all models in
    which the knowledge-base is true.

    Args:
        kb (list): the knowledge base, expressed as a list of CNF lists
        a (list): the sentence to be tested, expressed in CNF
        symbols (list): the list of all knowledge-base literals, in their positive forms

    Returns:
        True, if a is entailed by kb, False otherwise
    """
    return check_all_models(kb, a, symbols, [])

def check_all_models(kb: list, a: list, symbols: list, model: list):
    """Recursively check whether sentence a is true in all models in which the 
    kb evaluates to true

    Args:
        kb (list): the knowledge base, expressed as a list of CNF lists
        a (list): the sentence to be tested, expressed in CNF
        symbols (list): the list of all knowledge-base literals, in their positive forms
        model (list): the model of of symbol assignments to be tested

    Returns:
        True if the knowledge-base evaluates to False or both the knowledge-base and the 
        sentence evaluate to true, else False.
    """
    if not symbols:
        if check_truth(kb, model):
            return check_truth([a], model)  # Wrap `a` in a list
        else:
            return True
        
    else:
        p = symbols[0]
        remaining_symbols = [x for x in symbols if x != p]

        new_model_a = model + [p]
        result1 = check_all_models(kb, a, remaining_symbols, new_model_a)

        new_model_b = model + [-p]
        result2 = check_all_models(kb, a, remaining_symbols, new_model_b)

        return result1 and result2

def check_truth(kb_clauses: list, model: list):
    """checks the truth-value of a single clause against a sentence or knowledge-base.

    Args:
        kb_clauses (list): a list of knowledge-base clauses or a list representing a 
        CNF sentence
        model (list): the model of symbol assignments to be tested

    Returns:
        True if all clauses in kb_clauses are satified by a value in model, else False
    """
    for clause in kb_clauses:
        truth = False

        for value in clause:
            if value in model:
                truth = True
                break

        if truth == False:
            return False
        
    return True

def main():
    kb_1 = [[1, 2, 3],
           [-1, 2, 3],
           [-1, -2, -3],
           [-2, 3],
           [2, -3]]
    
    symbols_1 = [1, 2, 3]

    a_1 = [-3]  

    print(tt_entails(kb_1, a_1, symbols_1))  

main()

