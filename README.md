# Simple Calculator

A Python-based calculator application that provides basic arithmetic operations through both a command-line interface and a programmatic API.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power (exponentiation), modulo
- **Error Handling**: Proper handling of division by zero and invalid inputs
- **Interactive CLI**: User-friendly command-line interface
- **Comprehensive Testing**: Full test suite with 18 test cases
- **Clean Code**: Well-documented and organized code structure

## Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | `+` | `5 + 3` |
| Subtraction | `-` | `10 - 4` |
| Multiplication | `*` | `7 * 6` |
| Division | `/` | `15 / 3` |
| Power | `**` | `2 ** 3` |
| Modulo | `%` | `10 % 3` |

## Usage

### Command Line Interface

Run the calculator in interactive mode:

```bash
python calculator.py
```

Then enter calculations in the format: `number operator number`

Example session:
```
Welcome to the Simple Calculator!
Available operations: +, -, *, /, **, %
Type 'quit' to exit

Enter calculation (e.g., '5 + 3'): 5 + 3
Result: 5.0 + 3.0 = 8.0

Enter calculation (e.g., '5 + 3'): 10 / 2
Result: 10.0 / 2.0 = 5.0

Enter calculation (e.g., '5 + 3'): 2 ** 3
Result: 2.0 ** 3.0 = 8.0

Enter calculation (e.g., '5 + 3'): quit
Goodbye!
```

### Programmatic Usage

You can also use the Calculator class in your own Python code:

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # Returns 8
result = calc.subtract(10, 4)  # Returns 6
result = calc.multiply(7, 6)   # Returns 42
result = calc.divide(15, 3)    # Returns 5.0
result = calc.power(2, 3)      # Returns 8
result = calc.modulo(10, 3)    # Returns 1
```

## Error Handling

The calculator handles various error conditions gracefully:

- **Division by Zero**: Raises `ValueError` with descriptive message
- **Modulo by Zero**: Raises `ValueError` with descriptive message
- **Invalid Input**: Prompts user to enter valid format
- **Invalid Numbers**: Handles non-numeric input gracefully

Example:
```
Enter calculation (e.g., '5 + 3'): 5 / 0
Error: Cannot divide by zero
```

## Running Tests

Execute the test suite to verify all functionality:

```bash
python -m unittest test_calculator.py -v
```

The test suite includes 18 comprehensive test cases covering:
- All arithmetic operations with positive and negative numbers
- Decimal number calculations
- Error conditions (division by zero, modulo by zero)
- Edge cases and boundary conditions

## Files

- `calculator.py` - Main calculator implementation with CLI interface
- `test_calculator.py` - Comprehensive unit tests
- `README.md` - This documentation

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Development

The calculator is designed with clean code principles:

- **Single Responsibility**: Each method handles one specific operation
- **Error Handling**: Proper exception handling with descriptive messages
- **Documentation**: Comprehensive docstrings and comments
- **Testing**: High test coverage with meaningful test cases
- **User Experience**: Clear prompts and helpful error messages