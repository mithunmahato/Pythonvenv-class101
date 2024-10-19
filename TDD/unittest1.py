import unittest


def add_number(a,b):
    return a+b

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add_number(6,7)
        self.assertEqual(result,11)

    def test_add_negative_numbers(self):
        result = add_number(-6,-7)
        self.assertEqual(result,-13)
    
    def test_add_mixed_numbers(self):
        result = add_number(-6,7)
        self.assertEqual(result,1)
        
if __name__ == "__main__":
    unittest.main()
