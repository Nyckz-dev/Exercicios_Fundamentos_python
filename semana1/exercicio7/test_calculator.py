import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    
    def test_add_and_sum(self):
        self.calc.add([2, 4, 6])
        self.assertEqual(self.calc.sum_values(), 12)
    
    def test_average(self):
        self.calc.add([4, 6, 8])
        self.assertEqual(self.calc.average(), 6)
    
    def test_multiplication(self):
        self.calc.add([4, 2, 2])
        self.assertEqual(self.calc.multiplication(), 16)

if __name__ == "__main__":
    unittest.main()
    