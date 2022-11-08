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
