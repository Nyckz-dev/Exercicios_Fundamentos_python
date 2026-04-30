import unittest
from MultiplicationTable import MultiplicationTable
class Test(unittest.TestCase):
    
    def test_interval(self):
     result = MultiplicationTable().calculation(2, 3, 3)
     expected = [
        "2 x 1 = 2",
        "2 x 2 = 4",
        "2 x 3 = 6",
        "3 x 1 = 3",
        "3 x 2 = 6",
        "3 x 3 = 9"
     ]
     self.assertEqual(result, expected)

    def test_unique(self):
     result = MultiplicationTable().calculation(5,2,5)
     expected = [
          "5 x 1 = 5",
          "5 x 2 = 10"
        ]
     self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()