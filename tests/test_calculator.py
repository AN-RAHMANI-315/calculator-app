"""
Unit tests for calculator module.
"""

import pytest
import math
from src.calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_initialization(self):
        """Test calculator initialization."""
        assert self.calc.history == []

    # Basic Operations Tests
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = self.calc.add(5, 3)
        assert result == 8
        assert "5 + 3 = 8" in self.calc.history

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-5, -3)
        assert result == -8

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calc.add(5, -3)
        assert result == 2

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        result = self.calc.add(2.5, 3.7)
        assert result == pytest.approx(6.2)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        result = self.calc.subtract(10, 4)
        assert result == 6
        assert "10 - 4 = 6" in self.calc.history

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        result = self.calc.subtract(3, 8)
        assert result == -5

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        result = self.calc.multiply(4, 5)
        assert result == 20
        assert "4 * 5 = 20" in self.calc.history

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(5, 0)
        assert result == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        result = self.calc.multiply(-3, 4)
        assert result == -12

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        result = self.calc.divide(15, 3)
        assert result == 5
        assert "15 / 3 = 5.0" in self.calc.history

    def test_divide_with_remainder(self):
        """Test division with floating point result."""
        result = self.calc.divide(7, 2)
        assert result == 3.5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)

    # Advanced Operations Tests
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers."""
        result = self.calc.power(2, 3)
        assert result == 8
        assert "2 ^ 3 = 8" in self.calc.history

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = self.calc.power(5, 0)
        assert result == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = self.calc.power(2, -2)
        assert result == 0.25

    def test_square_root_positive_number(self):
        """Test square root of positive number."""
        result = self.calc.square_root(9)
        assert result == 3
        assert "√9 = 3.0" in self.calc.history

    def test_square_root_zero(self):
        """Test square root of zero."""
        result = self.calc.square_root(0)
        assert result == 0

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            self.calc.square_root(-1)

    def test_percentage_calculation(self):
        """Test percentage calculation."""
        result = self.calc.percentage(200, 15)
        assert result == 30
        assert "15% of 200 = 30.0" in self.calc.history

    def test_percentage_zero(self):
        """Test percentage calculation with zero."""
        result = self.calc.percentage(100, 0)
        assert result == 0

    def test_factorial_positive_integer(self):
        """Test factorial of positive integer."""
        result = self.calc.factorial(5)
        assert result == 120
        assert "5! = 120" in self.calc.history

    def test_factorial_zero(self):
        """Test factorial of zero."""
        result = self.calc.factorial(0)
        assert result == 1

    def test_factorial_negative_raises_error(self):
        """Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            self.calc.factorial(-1)

    def test_factorial_float_raises_error(self):
        """Test that factorial of float raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is only defined for integers"):
            self.calc.factorial(3.5)

    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        result = self.calc.modulo(10, 3)
        assert result == 1
        assert "10 % 3 = 1" in self.calc.history

    def test_modulo_zero_divisor_raises_error(self):
        """Test that modulo with zero divisor raises ValueError."""
        with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
            self.calc.modulo(10, 0)

    # History Tests
    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        self.calc.add(1, 2)
        self.calc.subtract(5, 3)
        self.calc.multiply(2, 4)
        
        history = self.calc.get_history()
        assert len(history) == 3
        assert "1 + 2 = 3" in history
        assert "5 - 3 = 2" in history
        assert "2 * 4 = 8" in history

    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 2)
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0

    def test_history_limit(self):
        """Test that history is limited to 100 operations."""
        # Add 105 operations
        for i in range(105):
            self.calc.add(i, 1)
        
        history = self.calc.get_history()
        assert len(history) == 100
        # First operation should be removed
        assert "0 + 1 = 1" not in history
        # Last operation should be present
        assert "104 + 1 = 105" in history


class TestConvenienceFunctions:
    """Test suite for convenience functions."""

    def test_add_function(self):
        """Test add convenience function."""
        result = add(3, 4)
        assert result == 7

    def test_subtract_function(self):
        """Test subtract convenience function."""
        result = subtract(10, 3)
        assert result == 7

    def test_multiply_function(self):
        """Test multiply convenience function."""
        result = multiply(3, 4)
        assert result == 12

    def test_divide_function(self):
        """Test divide convenience function."""
        result = divide(12, 3)
        assert result == 4

    def test_divide_function_zero_error(self):
        """Test divide convenience function with zero divisor."""
        with pytest.raises(ValueError):
            divide(5, 0)


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (2.5, 3.5, 6.0),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for addition operation."""
    calc = Calculator()
    result = calc.add(a, b)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3),
    (10, 5, 2),
    (7, 2, 3.5),
    (-10, 2, -5),
    (0, 1, 0),
])
def test_divide_parametrized(a, b, expected):
    """Parametrized test for division operation."""
    calc = Calculator()
    result = calc.divide(a, b)
    assert result == pytest.approx(expected)


@pytest.mark.slow
def test_large_number_operations():
    """Test operations with large numbers (marked as slow)."""
    calc = Calculator()
    large_num = 10**10
    result = calc.add(large_num, large_num)
    assert result == 2 * large_num
