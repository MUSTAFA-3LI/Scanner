# C Code Scanner

This project is a simple C code scanner implemented in Python. It reads C code from user input, tokenizes it, and displays the tokens found. The scanner identifies comments, keywords, identifiers, numbers, operators, special characters, and strings.

## Table of Contents

- [C Code Scanner](#c-code-scanner)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Features](#features)
  - [Usage](#usage)
  - [Code Overview](#code-overview)
    - [Dependencies](#dependencies)

## Prerequisites

Ensure you have the following installed:

1. **Python 3.12.3**
2. **Re Library**

## Features

- **Tokenization**: Identifies and categorizes different elements of C code.
- **User Input**: Accepts C code from the user until the keyword `SCAN` is entered.
- **Display Tokens**: Outputs the type, value, and line number of each token found.

## Usage

1. **Run the Script**: Execute the script using Python.
   ```sh
   python scanner.py

2. **Enter C Code**: Input your C code line by line. Type SCAN on a new line to finish.

Enter your C code below. Type 'SCAN' on a new line to finish:
```bash
int main() {
    // This is a comment
    printf("Hello, World!");
    return 0;
    }
SCAN
```

3. **View Tokens:** The script will display the tokens found in the input C code.

```bash
Tokens Found:
token's Type is : KEYWord, and Value is: 'int', at Line: 1
token's Type is : ID, and Value is: 'main', at Line: 1
token's Type is : spechial_CHaracter, and Value is: '(', at Line: 1
token's Type is : spechial_CHaracter, and Value is: ')', at Line: 1
token's Type is : spechial_CHaracter, and Value is: '{', at Line: 1
token's Type is : Comment, and Value is: '// This is a comment', at Line: 2
token's Type is : ID, and Value is: 'printf', at Line: 3
token's Type is : spechial_CHaracter, and Value is: '(', at Line: 3
token's Type is : STRING, and Value is: '"Hello, World!"', at Line: 3
token's Type is : spechial_CHaracter, and Value is: ')', at Line: 3
token's Type is : spechial_CHaracter, and Value is: ';', at Line: 3
token's Type is : KEYWord, and Value is: 'return', at Line: 4
token's Type is : Number, and Value is: '0', at Line: 4
token's Type is : spechial_CHaracter, and Value is: ';', at Line: 4
token's Type is : spechial_CHaracter, and Value is: '}', at Line: 5
```
![Screenshot](https://github.com/user-attachments/assets/25489e2f-c3af-48a9-9e30-d7df8f012410)

## Code Overview
1. **Token Definitions:** Regular expressions for different token types are defined in the tokens list.
2. **Pattern Compilation:** All token patterns are combined into a single pattern using re.compile.
3. **Functions:**
    1. parse_code(c_code): Parses the input C code and returns a list of tokens.
    2. get_user_code(): Prompts the user to enter C code and returns it as a single string.
    3. display_tokens(parsed_tokens): Displays the tokens found in the input C code.
    4. main(): Main function to run the scanner.


### Dependencies
Python 3.x
