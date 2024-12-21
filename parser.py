class Parser:
    def __init__(self):
        self.grammar = {}
        self.terminals = set()

    def add_rule(self, non_terminal, rule):
        if non_terminal not in self.grammar:
            self.grammar[non_terminal] = []
        self.grammar[non_terminal].append(rule)

        for char in rule:
            if char.islower():  # Identify terminals
                self.terminals.add(char)

    def is_simple_grammar(self):
        for non_terminal, rules in self.grammar.items():
            prefixes = set()
            for rule in rules:
                if rule == "":  # Reject epsilon (empty string) rules
                    print(f"The Grammar isn't simple: epsilon (ε) rule detected in {non_terminal}")
                    return False
                prefix = rule[0]
                if prefix in prefixes:  # Reject multiple rules starting with the same terminal
                    print(f"The Grammar isn't simple: multiple rules for {non_terminal} start with {prefix}")
                    print("\n--------------- Disjoint ----------------\n")
                    return False
                prefixes.add(prefix)
        return True

    def parse_sequence(self, sequence, start_symbol):
        self.input_sequence = sequence
        self.current_position = 0  # Ensures complete matching
        return self._parse_non_terminal(start_symbol) and self.current_position == len(sequence)

    def _parse_non_terminal(self, non_terminal):
        if non_terminal not in self.grammar:
            return False

        for rule in self.grammar[non_terminal]:
            saved_position = self.current_position
            if self._match_rule(rule):
                return True
            self.current_position = saved_position  # Backtrack if rule doesn't match

        return False

    def _match_rule(self, rule):
        for symbol in rule:
            if symbol.islower():  # Terminal
                if self.current_position < len(self.input_sequence) and self.input_sequence[self.current_position] == symbol:
                    self.current_position += 1
                else:
                    return False
            else:  # Non-Terminal
                if not self._parse_non_terminal(symbol):
                    return False
        return True


if __name__ == "__main__":
    while True:
        parser = Parser()  # Reinitialize the parser to clear previous states

        print("\n -----   Parsing for Simple Grammar  ------")
        print("\nEnter rules for two non-terminals.")
        non_terminals = []

        for i in range(2):
            non_terminal = input(f"Enter non-terminal {i + 1}: ").strip()
            non_terminals.append(non_terminal)

        for non_terminal in non_terminals:
            for j in range(2):
                rule = input(f"Enter rule {j + 1} for non-terminal '{non_terminal}': ").strip()
                parser.add_rule(non_terminal, rule)

        print("\nValidating grammar...")
        if parser.is_simple_grammar():
            print("The grammar is simple.")
            print("\n--------- ACCEPTED ----------")
        else:
            print("The grammar isn't simple.")
            print("\n--------- REJECTED ----------")
            continue

        while True:
            print("\n1 - Redefine Grammar Rules")
            print("2 - Test a String")
            print("3 - Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                break  # Exit the inner loop to redefine grammar rules

            elif choice == "2":
                sequence = input("Enter the string you want to test: ").strip()
                start_symbol = input("Enter the start symbol: ").strip() # Start symbol is the first non-terminal (S)

                if parser.parse_sequence(sequence, start_symbol):
                    print(f"Your input string '{sequence}' is ACCEPTED.")
                    print("\n----------  ACCEPTED -----------")
                else:
                    print(f"Your input string '{sequence}' is REJECTED.")
                    print("\n----------  REJECTED  -----------")
            elif choice == "3":
                exit()
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
