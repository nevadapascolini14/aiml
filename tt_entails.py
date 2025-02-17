"""Note that this works with CNF. If data is in a different format, convert
to CNF first."""

def tt_entails(kb: list, a: list, symbols: list):
    return check_all_models(kb, a, symbols, [])

def check_all_models(kb: list, a: list, symbols: list, model: list):
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

def check_truth(kb_clauses: list, model):
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

    a_1 = [-3]  # This is a single clause

    print(tt_entails(kb_1, a_1, symbols_1))  # Now correctly wrapped in a list in check_truth

main()

