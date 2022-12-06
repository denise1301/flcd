class Grammar:
    def __init__(self) -> None:
        self.N = None
        self.E = None
        self.P = None
        self.S = None

    def readGrammar(self, filename):
        with open(filename) as file:
            self.N = self.parseNonTerminals(file.readline())
            self.E = self.parseTerminals(file.readline())
            self.S = file.readline().split('=')[1].strip()
            self.P = self.parseProductions(self.parseNonTerminals(''.join([line for line in file])))

    def parseNonTerminals(self, line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    def parseTerminals(self, line):
        line = line[4:-1]
        return [value.strip() for value in line.strip()[1:-1].strip().split(',')]

    def parseProductions(self, rules):
        result = []
        for rule in rules:
            left_hand_side, right_hand_side = rule.split('->')
            left_hand_side = left_hand_side.strip()
            right_hand_side = [value.strip() for value in right_hand_side.split('|')]
            for value in right_hand_side:
                result.append((left_hand_side, value))
        return result

    def getProductionsForNonterminal(self, non_terminal):
        if non_terminal not in self.N:
            return False
        return [production for production in self.P if production[0] == non_terminal]

    def checkCFG(self):
        duplicate = None
        for p in self.P:
            if duplicate == p[0]:
                return False
            duplicate = p[0]
        return True

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'S = ' + str(self.S) + '\n' \
               + 'P = {\n' + '\n'.join([' => '.join(prod) for prod in self.P]) + ' \n}'
