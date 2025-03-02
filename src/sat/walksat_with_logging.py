import random
import pprint

def walksat(clauses: list, max_flips: int, p: float, model: list):
    print("\n=== Starting WalkSAT ===")
    print(f"Initial Model: {model}")
    print(f"Max Flips: {max_flips}, Probability p: {p}")

    for i in range(max_flips):
        false_clauses = []
        satisfied = True

        print("\n----------------------------------------")
        print(f"Iteration {i + 1}")
        print(f"Current Model: {model}")

        # Check if model satisfies all clauses
        for clause in clauses:
            # A clause is satisfied if at least one literal in it matches the model.
            if not any(litty in model for litty in clause):  # Clause is unsatisfied
                satisfied = False
                false_clauses.append(clause)

        if satisfied:
            print("\n✅ All clauses are satisfied! Found a solution:")
            pprint.pprint(model)
            return model

        print(f"❌ Unsatisfied clauses: {false_clauses}")

        # Pick a random false clause
        rand_clause = random.choice(false_clauses)
        print(f"Randomly selected false clause to fix: {rand_clause}")

        # Pick a random literal from that clause
        rand_lit = random.choice(list(rand_clause))
        print(f"Randomly selected literal to flip: {rand_lit}")

        # Flip the chosen literal in the model
        for j, item in enumerate(model):
            if item == rand_lit or item == -rand_lit:
                model[j] = -item  # Flip the sign
                print(f"Flipped literal {rand_lit} → {model[j]}")
                break  # Stop after the first occurrence is flipped

    print(f"\n❌ WalkSAT failed after {max_flips} flips. No satisfying assignment found.")
    return None


def main():
    print("\n=== Starting the SAT Solver (WalkSAT) ===")

    clauses = [{-1, 2, 3}, {2}]  # CNF Formula
    max_flips = 10000  # Max number of flips
    model = [-1, -2, -3]  # Initial assignment
    p = 0.5  # Probability of picking a random literal vs. greedy choice

    print("\n=== Initial Setup ===")
    print(f"CNF Clauses: {clauses}")
    print(f"Initial Model: {model}")
    print(f"Max Flips: {max_flips}, Probability p: {p}")

    result = walksat(clauses, max_flips, p, model)

    print("\n=== Final Result ===")
    if result:
        print("✅ Solution Found:")
        pprint.pprint(result)
    else:
        print("❌ No solution found.")


if __name__ == "__main__":
    main()