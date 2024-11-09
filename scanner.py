import re

tokens = [
    ('Comment', r'//.*|/\*[\s\S]*?\*/'),          # re for comments
    ('KEYWord', r'\b(?:int|float|char|if|else|while|for|return|void|struct|typedef|const)\b'),  # C keywords
    ('ID', r'\b[a-zA-Z_]\w*\b'),  # re for Identifiers .
    ('Number', r'\b\d+(\.\d+)?\b'),               # re for numbers values
    ('oprator', r'[+\-*/%!=<>|&]'),              # re for operators
    # re for spechial CHaracters
    ('spechial_CHaracter', r'[;,\(\){}]'),
    # String  (inside double quotes)
    ('STRING', r'"([^"\\]|\\.)*"'),
]

# join pattern to one pattern
combined_pattern = '|'.join(
    f'(?P<{name}>{pattern})' for name, pattern in tokens)
pattern_compiler = re.compile(combined_pattern)


def parse_code(c_code):
    parsed_tokens = []  # empty list to story token
    line_number = 1     # Track  line number to add to each token

    for match in pattern_compiler.finditer(c_code):
        token_type = match.lastgroup
        token_value = match.group()           # to story token's text

        if token_type not in ('COMMENT', 'WHITESPACE'):
            parsed_tokens.append((token_type, token_value, line_number))

        # Update line number
        if '\n' in token_value:
            # update line number if user enter new line
            line_number += token_value.count('\n')
    return parsed_tokens


def get_user_code():  # this function accept user input
    print("Enter your C code below. Type 'SCAN' on a new line to finish:")

    code_lines = []
    while True:
        line = input()  # get each line of input
        if line.strip().upper() == "SCAN":  # to make sure word SCAN will be upper
            break
        code_lines.append(line)

    return "\n".join(code_lines)  # join lines into a single text

#  to display tokens for user


def display_tokens(parsed_tokens):
    print("\nTokens Found:")
    for token in parsed_tokens:
        print(
            f"token's Type is : {token[0]}, and Value is: '{token[1]}', at Line: {token[2]}")


def main():
    c_code = get_user_code()  # run our functions
    tokens_found = parse_code(c_code)
    display_tokens(tokens_found)


if __name__ == "__main__":
    main()
