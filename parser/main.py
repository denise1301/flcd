from parser.Grammar import Grammar


def main():
    g = Grammar()
    g.readGrammar("g1.txt")
    print(g)
    print('Is CGF? ' + g.checkCFG().__str__())


main()
