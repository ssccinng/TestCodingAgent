"""
A simple calculator implementation with basic arithmetic operations.
"""

class Calculator:
    """A calculator class that provides basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first number."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise first number to the power of second number."""
        return a ** b
    
    def modulo(self, a, b):
        """Get remainder of division of first number by second number."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        return a % b


def main():
    """Main function to run the calculator in interactive mode."""
    calc = Calculator()
    
    print("Welcome to the Simple Calculator!")
    print("Available operations: +, -, *, /, **, %")
    print("Type 'quit' to exit")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter calculation (e.g., '5 + 3'): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please use format: number operator number")
                continue
            
            try:
                num1 = float(parts[0])
                operator = parts[1]
                num2 = float(parts[2])
            except ValueError:
                print("Invalid numbers. Please enter valid numbers.")
                continue
            
            # Perform calculation
            result = None
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            elif operator == '**':
                result = calc.power(num1, num2)
            elif operator == '%':
                result = calc.modulo(num1, num2)
            else:
                print(f"Unsupported operator: {operator}")
                continue
            
            # Display result
            print(f"Result: {num1} {operator} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()