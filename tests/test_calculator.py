# -*- coding: utf-8 -*-
import unittest
import os
import sys

# Thêm thư mục gốc vào sys.path để có thể import từ app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import multiply

class TestCalculator(unittest.TestCase):
    def test_multiply_3_4(self):
        """Check multiply(3, 4) == 12."""
        print("\n[Test Log] Running test case: multiply(3, 4) == 12")
        result = multiply(3, 4)
        self.assertEqual(result, 12, "Lỗi! Phép nhân 3 * 4 phải bằng 12")
        print(f"[Test Log] Success: {result} == 12")
        
    def test_multiply_zero(self):
        """Check multiply by zero."""
        self.assertEqual(multiply(0, 99), 0)
        self.assertEqual(multiply(99, 0), 0)
        
    def test_multiply_negative(self):
        """Check multiply with negative numbers."""
        self.assertEqual(multiply(-5, 5), -25)
        self.assertEqual(multiply(-5, -5), 25)
        
    def test_multiply_floats(self):
        """Check multiply with floats."""
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

if __name__ == '__main__':
    unittest.main()
