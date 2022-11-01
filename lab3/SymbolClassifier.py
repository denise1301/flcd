class SymbolClassifier:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.classify()

    def classify(self) -> None:
        with open('lab3/Tokens.in', 'r') as f:
            f.readline()
            for i in range(7):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
            for i in range(15):
                self.operators.append(f.readline().strip())
            for i in range(9):
                self.reservedWords.append(f.readline().strip())