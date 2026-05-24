import unittest
import math

class TestCalculator(unittest.TestCase):
    def test_basic_math(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(10 - 3, 7)
        self.assertEqual(5 * 6, 30)
        self.assertEqual(8 / 2, 4)

    def test_advanced_math(self):
        self.assertEqual(math.sqrt(16), 4)
        self.assertEqual(math.factorial(5), 120)
        self.assertAlmostEqual(math.sin(math.pi/2), 1.0, places=5)
        self.assertAlmostEqual(math.log(math.e), 1.0, places=5)

if __name__ == "__main__":
    unittest.main()
