from collections import defaultdict

"""model_exists = number of clauses
   example = enumerate clauses, remember positive literals <= 1. """

class ForwardChaining:
    def __init__(self):
        self.clauses = []
        self.model = defaultdict(bool)  # Initialize with all symbols as False

    def forward_chaining(self, n):
        """
        Performs forward chaining on a set of clauses.

        Args:
            n: The number of propositional symbols.

        Returns:
            True if a model is found, False otherwise.
        """

        # Check horn clauses and clause numbers
        for clause in self.clauses:
            pos_lits = sum(1 for lit in clause if lit > 0)
            assert pos_lits <= 1, "At most one positive literal is allowed in each clause."
            for lit in clause:
                assert -n <= lit <= n, "Found reference to variable larger than n."

        while True:
            fixpoint = True
            for clause in self.clauses:
                all_neg_true = all(not self.model[-lit] for lit in clause if lit < 0) 
                if all_neg_true:
                    for lit in clause:
                        if lit > 0:
                            if not self.model[lit]:
                                self.model[lit] = True
                                fixpoint = False
                                print(f"Inferred {lit} with clause {clause}")
                            break
                    else:
                        # This is a goal clause
                        print(f"No models satisfy all clauses simultaneously. False goal clause: {clause}")
                        return False

            if fixpoint:
                break

        print("Model:")
        for i in range(1, n + 1):
            print(f"Variable {i} = {self.model[i]}")
        return True

    def add_clause(self, c):
        self.clauses.append(c)

    def reset_clauses(self):
        self.clauses = []

def example():
    # The following is the CNF of Figure 7.16 in AIMA
    # Symbols A, B, L, M, P, Q are numbered 1..6.
    fc = ForwardChaining()

    fc.add_clause([-7, -10, -5, 13])
    fc.add_clause([-7, -10, -11, 14])
    fc.add_clause([-8, -9, -12, 15])
    fc.add_clause([-9, -12, -4, 16])
    fc.add_clause([-11, -10, -3, 17])
    fc.add_clause([5])
    fc.add_clause([7])
    fc.add_clause([10])
    fc.add_clause([11])

    # Call forward chaining. 17 is the number of propositional symbols, which must be
    # numbered 1..17.
    model_exists = fc.forward_chaining(17)
    print(f"Model exists: {model_exists}")

if __name__ == "__main__":
    example()