class FiniteAutomata:

    def __init__(self, states: list, alphabet: list, initial, final: list, delta: dict):
        self.Q = states  # states
        self.E = alphabet  # alphabet
        self.delta = delta  # transition function
        self.q0 = initial  # initial state
        self.F = final  # final states

    def __str__(self):
        return "States = { " + ', '.join(self.Q) + " }\n" \
               "Alphabet = { " + ', '.join(self.E) + " }\n" \
               "Initial State = { " + self.q0 + " }\n" \
               "Transitions = { " + str(self.delta) + " }\n" \
               "Final States = { " + ', '.join(self.F) + " }\n"

    def isDFA(self):
        for elem in self.delta.keys():
            if len(self.delta[elem]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        print(sequence)
        if self.isDFA():
            current = self.q0
            for symbol in sequence:
                if (current, symbol) in self.delta.keys():
                    current = self.delta[(current, symbol)][0]
                else:
                    return False
            return current in self.F
        return False
