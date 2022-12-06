class Parser:
    def __init__(self, g):
        self.grammar = g
        self.parseTable = []
        self.productionsRhs = []
        self.generateParseTable()
