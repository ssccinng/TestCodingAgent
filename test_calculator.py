"""
Unit tests for the Calculator class.
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(0, 5), 5)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, 3), 1)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_add_decimals(self):
        """Test addition with decimal numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(3, 5), -2)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(1, 7), 7)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(0, -5), 0)
    
    def test_multiply_decimals(self):
        """Test multiplication with decimal numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 3.0), 7.5, places=7)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.3), 0.03, places=7)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(10, -2), -5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
        
        with self.assertRaises(ValueError):
            self.calc.divide(-5, 0)
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        self.assertEqual(self.calc.power(1, 100), 1)
    
    def test_power_negative_numbers(self):
        """Test power operation with negative numbers."""
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(2, -2), 0.25)
    
    def test_power_decimals(self):
        """Test power operation with decimal numbers."""
        self.assertAlmostEqual(self.calc.power(2.5, 2), 6.25, places=7)
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0, places=7)
    
    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 5), 0)
        self.assertEqual(self.calc.modulo(7, 2), 1)
    
    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)
        self.assertEqual(self.calc.modulo(-10, -3), -1)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(5, 0)
        self.assertEqual(str(context.exception), "Cannot perform modulo with zero")
    
    def test_modulo_decimals(self):
        """Test modulo operation with decimal numbers."""
        self.assertAlmostEqual(self.calc.modulo(5.5, 2.0), 1.5, places=7)
        self.assertAlmostEqual(self.calc.modulo(7.8, 2.5), 0.3, places=7)


if __name__ == "__main__":
    unittest.main()