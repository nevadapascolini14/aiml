from collections import deque

def forward_chaining(kb: list, initial_facts: list):
    """Forward chaining implementation using horn clauses to infer facts.

    Args:
        kb (list): Knowledge-base rules, expressed in CNF.
        initial_facts (list): Atomic facts, expressed as literals.

    Returns:
        str: A combined list of initial and derived facts.
    """
    
    facts = set(initial_facts)
    agenda = deque(initial_facts)

    while agenda:
        fact = agenda.popleft()

        for clause in kb:
            antecedents = [lit for lit in clause if lit < 0]
            consequents = [lit for lit in clause if lit > 0]

            if all(-lit in facts for lit in antecedents):  # Check if antecedents are satisfied
                if consequents:  # Ensure there's a consequent to derive
                    new_fact = consequents[0]
                    if new_fact not in facts:
                        facts.add(new_fact)
                        agenda.append(new_fact)

    return "Satisfiable: Facts derived: " + str(facts)

def main():
    kb_1 = [[-7, -10, -5, 13],
            [-7, -10, -11, 14],
            [-8, -9, -12, 15],
            [-9, -12, -4, 16],
            [-11, -10, -3, 17]]
    
    if_1 = [5, 7, 10, 11]
    
    print(forward_chaining(kb_1, if_1))

if __name__ == "__main__":
    main()