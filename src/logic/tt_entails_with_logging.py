def tt_check_all(kb, alpha, symbols, model):
    

def pl_true(sentence, model):
    if len(sentence)==1:
        return model.get(sentence, False)
    elif "-" in sentence:
        return not pl_true(sentence[0]("-",""), model)
    elif "," in sentence:
        return pl_true(sentence[0], model) and pl_true(sentence[1], model)
    
    
    FUNCTION PL-TRUE?(sentence, model):
    IF sentence is a single propositional symbol:
        RETURN LOOKUP(sentence, model)  # Get its truth value from the model

    ELSE IF sentence is a NOT (¬P):
        RETURN NOT PL-TRUE?(P, model)  # Recursively evaluate negation

    ELSE IF sentence is an AND (P ∧ Q):
        RETURN PL-TRUE?(P, model) AND PL-TRUE?(Q, model)  # Both must be True

    ELSE IF sentence is an OR (P ∨ Q):
        RETURN PL-TRUE?(P, model) OR PL-TRUE?(Q, model)  # At least one must be True

    ELSE IF sentence is an IMPLICATION (P → Q):
        RETURN (NOT PL-TRUE?(P, model)) OR PL-TRUE?(Q, model)  # Equivalent to ¬P ∨ Q

    ELSE IF sentence is a BICONDITIONAL (P ↔ Q):
        RETURN PL-TRUE?(P, model) == PL-TRUE?(Q, model)  # True if both are same

    ELSE:
        ERROR: "Invalid logical sentence"


def tt_entails(kg, alpha):
    
    