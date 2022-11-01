from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable


class ScannerResult:

    def __init__(self):
        self.ST = SymbolTable(20)
        self.PIF = ProgramInternalForm()
        self.scanner = Scanner()

    def compute_results(self, file_name: str):
        exceptionMessage = ""
        reserved_words = self.scanner.get_reserved_words()
        separators = self.scanner.get_separators()
        operators = self.scanner.get_operators()

        with open(file_name, 'r') as file:
            line_counter = 0
            for line in file:
                position = 0
                line_counter += 1
                tokens = self.scanner.get_tokens(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] == ' ':  # ignore adding spaces to the pif
                            continue
                        self.PIF.add(tokens[i], "(Line: " + str(line_counter) + "; Column: " + str(position + 1) + ")")

                    elif self.scanner.is_identifier(tokens[i]):
                        self.ST.add(tokens[i], 1)
                        self.PIF.add(tokens[i], "(Line: " + str(line_counter) + "; Column: " + str(position + 1) + ")")
                    elif self.scanner.is_constant(tokens[i]):
                        self.ST.add(extra + tokens[i], 1)
                        extra = ''
                        self.PIF.add(extra + tokens[i],
                                     "(Line: " + str(line_counter) + "; Column: " + str(position + 1) + ")")
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            line_counter) + " column: " + str(position + 1) + "\n"
                    position += len(tokens[i])

        with open('lab3/st.out', 'w') as writer:
            writer.write(str(self.ST))
        with open('lab3/pif.out', 'w') as writer:
            writer.write(str(self.PIF))
        if exceptionMessage == '':
            print("Lexically correct")
        else:
            print(exceptionMessage)


if __name__ == '__main__':
    scanner_result = ScannerResult()
    scanner_result.compute_results("lab3/p1.txt")
    scanner_result.compute_results("lab3/p1err.txt")
    scanner_result.compute_results("lab3/p2.txt")
    scanner_result.compute_results("lab3/p3.txt")
