"""
Integration tests for calculator application.
"""

import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


@pytest.mark.integration
class TestCalculatorIntegration:
    """Integration tests for calculator workflows."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_complex_calculation_workflow(self):
        """Test a complex series of calculations."""
        # Simulate: ((10 + 5) * 2) / 3 = 10
        step1 = self.calc.add(10, 5)  # 15
        step2 = self.calc.multiply(step1, 2)  # 30
        step3 = self.calc.divide(step2, 3)  # 10
        
        assert step3 == 10
        assert len(self.calc.get_history()) == 3

    def test_scientific_calculations(self):
        """Test scientific calculation workflow."""
        # Calculate area of circle: π * r²
        radius = 5
        radius_squared = self.calc.power(radius, 2)  # 25
        pi_approx = 3.14159
        area = self.calc.multiply(pi_approx, radius_squared)  # ~78.54
        
        assert area == pytest.approx(78.53975, abs=0.01)

    def test_financial_calculations(self):
        """Test financial calculation workflow."""
        # Calculate compound interest: A = P(1 + r)^t
        principal = 1000
        rate = 0.05  # 5%
        years = 3
        
        # (1 + rate)
        rate_plus_one = self.calc.add(1, rate)  # 1.05
        # (1 + rate)^years
        compound_factor = self.calc.power(rate_plus_one, years)  # ~1.157625
        # Final amount
        final_amount = self.calc.multiply(principal, compound_factor)
        
        assert final_amount == pytest.approx(1157.625, abs=0.01)

    def test_error_recovery_workflow(self):
        """Test that calculator can recover from errors."""
        # Normal operation
        result1 = self.calc.add(5, 3)
        assert result1 == 8
        
        # Error operation
        with pytest.raises(ValueError):
            self.calc.divide(10, 0)
        
        # Calculator should still work after error
        result2 = self.calc.subtract(10, 4)
        assert result2 == 6
        
        # History should contain successful operations only
        history = self.calc.get_history()
        assert "5 + 3 = 8" in history
        assert "10 - 4 = 6" in history
        assert len([h for h in history if "/ 0" in h]) == 0

    def test_mixed_operation_types(self):
        """Test mixing different types of operations."""
        # Start with basic operations
        result1 = self.calc.add(10, 5)  # 15
        result2 = self.calc.subtract(result1, 3)  # 12
        
        # Advanced operations
        result3 = self.calc.square_root(result2)  # ~3.464
        result4 = self.calc.power(result3, 2)  # Should be close to 12
        
        # Check final result is close to original
        assert result4 == pytest.approx(12, abs=0.001)

    def test_percentage_calculations_workflow(self):
        """Test percentage calculation workflows."""
        base_value = 200
        
        # Calculate 15% of 200
        percent_result = self.calc.percentage(base_value, 15)  # 30
        
        # Add the percentage to the base (115% of original)
        total_with_percent = self.calc.add(base_value, percent_result)  # 230
        
        # Verify this equals 115% of original
        direct_calculation = self.calc.percentage(base_value, 115)  # 230
        
        assert total_with_percent == direct_calculation

    def test_factorial_workflow(self):
        """Test factorial calculations in workflow."""
        # Calculate 5! / 3! = 5 * 4 = 20
        fact_5 = self.calc.factorial(5)  # 120
        fact_3 = self.calc.factorial(3)  # 6
        result = self.calc.divide(fact_5, fact_3)  # 20
        
        assert result == 20

    def test_modulo_workflow(self):
        """Test modulo operations in workflow."""
        # Check if a number is even using modulo
        test_number = 42
        remainder = self.calc.modulo(test_number, 2)
        
        assert remainder == 0  # 42 is even
        
        # Test with odd number
        odd_number = 43
        odd_remainder = self.calc.modulo(odd_number, 2)
        
        assert odd_remainder == 1  # 43 is odd

    def test_history_preservation_during_workflow(self):
        """Test that history is preserved during complex workflows."""
        operations = [
            (self.calc.add, 5, 3),
            (self.calc.multiply, 2, 4),
            (self.calc.divide, 10, 2),
            (self.calc.power, 2, 3),
            (self.calc.square_root, 16),
        ]
        
        for operation in operations:
            if len(operation) == 3:
                operation[0](operation[1], operation[2])
            else:
                operation[0](operation[1])
        
        history = self.calc.get_history()
        assert len(history) == 5
        assert "5 + 3 = 8" in history
        assert "2 * 4 = 8" in history
        assert "10 / 2 = 5.0" in history
        assert "2 ^ 3 = 8" in history
        assert "√16 = 4.0" in history

    @pytest.mark.slow
    def test_performance_workflow(self):
        """Test calculator performance with many operations."""
        # Perform 1000 operations
        for i in range(1000):
            self.calc.add(i, 1)
        
        # Verify only last 100 are kept in history
        history = self.calc.get_history()
        assert len(history) == 100
        
        # Last operation should be 999 + 1 = 1000
        assert "999 + 1 = 1000" in history[-1]
