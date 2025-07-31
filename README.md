# Calculator App

A modern, user-friendly web-based calculator that performs basic arithmetic operations including addition, subtraction, multiplication, and division. The calculator supports both integer and floating-point numbers with proper error handling.

## Features

- **Basic Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (×), Division (/)
- **Number Support**: Both integers and floating-point numbers
- **User-Friendly Interface**: Clean, modern design with responsive layout
- **Keyboard Support**: Use your keyboard for input (numbers, operators, Enter for equals, Escape for clear)
- **Error Handling**: Proper handling of division by zero and invalid operations
- **Advanced Functions**: Clear (C), Clear Entry (CE), Backspace (⌫)
- **Chain Operations**: Perform multiple operations in sequence

## Usage

### Opening the Calculator

1. Open `index.html` in any modern web browser
2. The calculator will load with a clean interface ready for use

### Basic Operations

1. **Enter Numbers**: Click number buttons (0-9) or use keyboard
2. **Decimal Numbers**: Click the decimal point (.) button or press "." on keyboard
3. **Operations**: Click operation buttons (+, -, ×, /) or use keyboard
4. **Calculate**: Click equals (=) button or press Enter
5. **Clear All**: Click C button or press Escape
6. **Clear Entry**: Click CE button to clear current input
7. **Backspace**: Click ⌫ button or press Backspace to delete last character

### Keyboard Shortcuts

- **Numbers**: 0-9 keys
- **Decimal**: Period (.) key
- **Addition**: Plus (+) key
- **Subtraction**: Minus (-) key
- **Multiplication**: Asterisk (*) key
- **Division**: Forward slash (/) key
- **Calculate**: Enter or Equals (=) key
- **Clear All**: Escape key
- **Backspace**: Backspace key

## Examples

### Basic Calculations
- `5 + 3 = 8`
- `10 - 4 = 6`
- `6 × 7 = 42`
- `15 ÷ 3 = 5`

### Decimal Calculations
- `2.5 + 3.7 = 6.2`
- `10.5 ÷ 2 = 5.25`

### Chain Operations
- `2 + 3 × 4 = 20` (calculates as (2 + 3) × 4)

## Error Handling

The calculator includes robust error handling for:

- **Division by Zero**: Displays "Cannot divide by zero"
- **Invalid Results**: Handles overflow and invalid operations
- **Multiple Decimal Points**: Prevents entry of multiple decimal points in one number
- **Invalid Input**: Ignores invalid button presses

## File Structure

```
calculator-app/
├── index.html          # Main calculator interface
├── styles.css          # CSS styling for the calculator
├── calculator.js       # JavaScript logic and functionality
├── test.html          # Test suite for validation
└── README.md          # This documentation file
```

## Technical Details

### Browser Compatibility
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive design
- No external dependencies required

### Features Implemented
- Object-oriented JavaScript architecture
- CSS Grid layout for button arrangement
- Event handling for both mouse and keyboard input
- Comprehensive test suite with 15+ test cases
- Error state management
- Floating-point precision handling

## Testing

Open `test.html` in a web browser to run the automated test suite. The tests validate:

- Basic arithmetic operations
- Decimal number handling
- Error conditions (division by zero)
- Chain operations
- Input validation
- Clear and delete functions

## Development

The calculator is built with vanilla HTML, CSS, and JavaScript for maximum compatibility and performance. No build process or external dependencies are required.

### Code Organization
- **HTML**: Semantic structure with accessibility considerations
- **CSS**: Modern styling with CSS Grid and Flexbox
- **JavaScript**: Class-based architecture with comprehensive error handling

## License

This calculator app is provided as-is for educational and practical use.