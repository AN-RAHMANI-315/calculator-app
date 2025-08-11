"""
Calculator module providing basic and advanced mathematical operations.
"""

import math
from typing import Union


class Calculator:
    """A comprehensive calculator class with basic and advanced operations."""

    def __init__(self):
        """Initialize calculator with operation history."""
        self.history = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = base ** exponent
        self._add_to_history(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, number: Union[int, float]) -> float:
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(number)
        self._add_to_history(f"√{number} = {result}")
        return result

    def percentage(self, value: Union[int, float], percent: Union[int, float]) -> Union[int, float]:
        """Calculate percentage of a value."""
        result = (value * percent) / 100
        self._add_to_history(f"{percent}% of {value} = {result}")
        return result

    def factorial(self, n: int) -> int:
        """Calculate factorial of a number."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(n, int):
            raise ValueError("Factorial is only defined for integers")
        result = math.factorial(n)
        self._add_to_history(f"{n}! = {result}")
        return result

    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate modulo (remainder) of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")
        result = a % b
        self._add_to_history(f"{a} % {b} = {result}")
        return result

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()

    def _add_to_history(self, operation: str) -> None:
        """Add operation to history."""
        self.history.append(operation)
        # Keep only last 100 operations
        if len(self.history) > 100:
            self.history.pop(0)


# Convenience functions for direct use
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers (convenience function)."""
    calc = Calculator()
    return calc.add(a, b)


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a (convenience function)."""
    calc = Calculator()
    return calc.subtract(a, b)


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers (convenience function)."""
    calc = Calculator()
    return calc.multiply(a, b)


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide a by b (convenience function)."""
    calc = Calculator()
    return calc.divide(a, b)
