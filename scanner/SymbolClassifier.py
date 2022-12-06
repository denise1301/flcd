class SymbolClassifier:

    def __init__(self):
        self.separators = []
        self.operators = []
        self.reservedWords = []
        self.all = []
        self.classify()

    def classify(self) -> None:
        with open('scanner/Tokens.in', 'r') as f:
            f.readline()
            for i in range(7):
                separator = f.readline().strip()
                if separator == "space":
                    separator = " "
                self.separators.append(separator)
                self.all.append(separator)
            for i in range(15):
                operator = f.readline().strip()
                self.operators.append(operator)
                self.all.append(operator)
            for i in range(10):
                reservedWord = f.readline().strip()
                self.reservedWords.append(reservedWord)
                self.all.append(reservedWord)
