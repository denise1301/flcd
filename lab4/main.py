from lab4.FiniteAutomata import FiniteAutomata


def read(file_name):
    with open(file_name) as file:
        states = file.readline().strip().split(' ')[2:]
        alphabet = file.readline().strip().split(' ')[2:]
        initial = file.readline().strip().split(' ')[2:][0]
        final = file.readline().strip().split(' ')[2:]

        file.readline()
        delta = {}
        for line in file:
            split = line.strip().split('=>')
            source = split[0].strip().replace('(', '').replace(')', '').split(',')[0]
            route = split[0].strip().replace('(', '').replace(')', '').split(',')[1]
            destination = split[1].strip()

            if (source, route) in delta.keys():
                delta[(source, route)].append(destination)
            else:
                delta[(source, route)] = [destination]

        return FiniteAutomata(states, alphabet, initial, final, delta)


def displayMenu():
    print("0. Exit")
    print("1. Show everything")
    print("2. Show States")
    print("3. Show Alphabet")
    print("4. Show Transitions")
    print("5. Show Initial State")
    print("6. Show Final States")


def run():
    finite_automata = read('FA.in')
    done = False
    while not done:
        displayMenu()
        print(">>")
        command = input()
        match command:
            case "0":
                done = True
                break
            case "1":
                print(finite_automata)
            case "2":
                print(finite_automata.Q)
            case "3":
                print(finite_automata.E)
            case "4":
                print(finite_automata.delta)
            case "5":
                print(finite_automata.q0)
            case "6":
                print(finite_automata.F)
            case _:
                print("Invalid command!\n")


if __name__ == '__main__':
    run()
