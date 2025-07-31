// Calculator App JavaScript

class Calculator {
    constructor() {
        this.display = document.getElementById('display');
        this.currentInput = '';
        this.operator = '';
        this.previousInput = '';
        this.shouldResetDisplay = false;
    }

    // Update the display
    updateDisplay(value) {
        this.display.value = value;
        this.display.classList.remove('error');
    }

    // Show error in display
    showError(message) {
        this.display.value = message;
        this.display.classList.add('error');
        this.shouldResetDisplay = true;
    }

    // Clear all
    clear() {
        this.currentInput = '';
        this.operator = '';
        this.previousInput = '';
        this.shouldResetDisplay = false;
        this.updateDisplay('');
    }

    // Clear current entry
    clearEntry() {
        this.currentInput = '';
        this.updateDisplay('');
    }

    // Delete last character
    deleteLast() {
        if (this.shouldResetDisplay) {
            this.clear();
            return;
        }
        
        this.currentInput = this.currentInput.slice(0, -1);
        this.updateDisplay(this.currentInput);
    }

    // Append number or decimal point to display
    appendNumber(num) {
        if (this.shouldResetDisplay) {
            this.clear();
        }

        // Handle decimal point
        if (num === '.') {
            if (this.currentInput.includes('.')) {
                return; // Don't allow multiple decimal points
            }
            if (this.currentInput === '') {
                this.currentInput = '0.';
            } else {
                this.currentInput += '.';
            }
        } else {
            // Handle leading zeros
            if (this.currentInput === '0' && num !== '.') {
                this.currentInput = num;
            } else {
                this.currentInput += num;
            }
        }

        this.updateDisplay(this.currentInput);
    }

    // Handle operator input
    setOperator(op) {
        if (this.shouldResetDisplay) {
            this.clear();
        }

        if (this.currentInput === '' && this.previousInput === '') {
            return; // Don't allow operator as first input
        }

        if (this.currentInput === '' && this.previousInput !== '') {
            // Just change the operator
            this.operator = op;
            return;
        }

        if (this.previousInput !== '' && this.currentInput !== '' && this.operator !== '') {
            // Calculate intermediate result
            this.calculate();
            // After intermediate calculation, reset the flag since we're continuing
            this.shouldResetDisplay = false;
        }

        this.operator = op;
        this.previousInput = this.currentInput;
        this.currentInput = '';
    }

    // Perform calculation
    calculate() {
        if (this.shouldResetDisplay) {
            this.clear();
            return;
        }

        if (this.previousInput === '' || this.currentInput === '' || this.operator === '') {
            return;
        }

        const prev = parseFloat(this.previousInput);
        const current = parseFloat(this.currentInput);
        let result;

        // Validate numbers
        if (isNaN(prev) || isNaN(current)) {
            this.showError('Error');
            return;
        }

        switch (this.operator) {
            case '+':
                result = prev + current;
                break;
            case '-':
                result = prev - current;
                break;
            case '*':
                result = prev * current;
                break;
            case '/':
                if (current === 0) {
                    this.showError('Cannot divide by zero');
                    return;
                }
                result = prev / current;
                break;
            default:
                return;
        }

        // Handle floating point precision
        result = Math.round((result + Number.EPSILON) * 100000000) / 100000000;

        // Check for infinity or invalid results
        if (!isFinite(result)) {
            this.showError('Result too large');
            return;
        }

        this.currentInput = result.toString();
        this.operator = '';
        this.previousInput = '';
        this.shouldResetDisplay = true;
        this.updateDisplay(this.currentInput);
    }
}

// Initialize calculator
const calc = new Calculator();

// Global functions for HTML onclick handlers
function clearDisplay() {
    calc.clear();
}

function clearEntry() {
    calc.clearEntry();
}

function deleteLast() {
    calc.deleteLast();
}

function appendToDisplay(value) {
    if (['+', '-', '*', '/'].includes(value)) {
        calc.setOperator(value);
    } else {
        calc.appendNumber(value);
    }
}

function calculate() {
    calc.calculate();
}

// Keyboard support
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    // Prevent default behavior for calculator keys
    if (/[0-9+\-*/.=]/.test(key) || key === 'Enter' || key === 'Escape' || key === 'Backspace') {
        event.preventDefault();
    }

    // Handle number keys
    if (/[0-9.]/.test(key)) {
        appendToDisplay(key);
    }
    
    // Handle operator keys
    else if (['+', '-', '*'].includes(key)) {
        appendToDisplay(key);
    }
    
    // Handle division (both / and ÷)
    else if (key === '/') {
        appendToDisplay('/');
    }
    
    // Handle equals and enter
    else if (key === '=' || key === 'Enter') {
        calculate();
    }
    
    // Handle escape and clear
    else if (key === 'Escape') {
        clearDisplay();
    }
    
    // Handle backspace
    else if (key === 'Backspace') {
        deleteLast();
    }
});

// Prevent right-click context menu on calculator
document.querySelector('.calculator').addEventListener('contextmenu', function(e) {
    e.preventDefault();
});