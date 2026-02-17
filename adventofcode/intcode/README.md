# Intcode

Interpreter for the Intcode programming language used in Advent of Code 2019.

## Installation

The package is automatically installed with the adventofcode package:

```bash
pip install -e .
```

## Usage

```python
from adventofcode.intcode import interpret_intcode, Interpreter

# Simple execution
result = interpret_intcode([1, 0, 0, 0, 99])
print(result.memory)  # [2, 0, 0, 0, 99]

# With stdin
result = interpret_intcode([3, 0, 99, 0], stdin=[42])
print(result.stdout)  # [42]

# For more control, use the Interpreter class
interpreter = Interpreter([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])
interpreter.stdin = [8]
interpreter.interpret()
print(interpreter.stdout)  # [1]
```

## API

### `interpret_intcode(program, stdin=[])`
Execute an Intcode program and return the Interpreter object.

- `program`: List of integers representing the Intcode program
- `stdin`: List of integers to use as input

### `class Interpreter`
Intcode interpreter with more control options.

- `stdin`: List of integers for input
- `stdout`: List of integers for output
- `memory`: The program memory
- `halted`: Boolean indicating if the program has halted
- `interpret(break_on_input=False, break_on_output=True)`: Run the interpreter

### Enums
- `Operation`: ADDITION, MULTIPLICATION, INPUT, OUTPUT, JMP_IF_TRUE, JMP_IF_FALSE, LESS_THAN, EQUALS, BASE, TERMINATION
- `Mode`: POSITION, IMMEDIATE, RELATIVE

