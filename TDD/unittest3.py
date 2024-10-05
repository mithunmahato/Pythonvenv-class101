import unittest

# Step 2: Create a function to be tested
def multiply_numbers(a, b):
    return a * b

class TestMultiplyNumbers(unittest.TestCase):

    def setUp(self): 
        print("Setting up the test environment...")
        self.num1 = 5
        self.num2 = 10

    def test_multiply_positive_numbers(self):
        result = multiply_numbers(self.num1, self.num2)
        self.assertEqual(result, 50)

    def test_multiply_by_zero(self):
        result = multiply_numbers(self.num1, 0)
        self.assertEqual(result, 0)

    def test_multiply_negative_numbers(self):
        result = multiply_numbers(-3, -4)
        self.assertEqual(result, 12)

    # Step 6: Define the tearDown() method (optional)
    def tearDown(self):
        print("Cleaning up the test environment...")
        del self.num1
        del self.num2


if __name__ == '__main__':
    unittest.main()
