import unittest

def multiply_num(a,b):
    return a*b

class TestMultiplynumber(unittest.TestCase):


    def setUp(self):
        print("Setting up the enviroment")

        self.a = 5
        self.b = 6

    def test_multiply_postive_numbers(self):
        result = multiply_num(self.a, self.b)
        self.assertEqual(result,30)
    
    def test_multiply_mixed_numbers(self):
        result = multiply_num(-3,4)
        self.assertEqual(result,-12)

    def test_multiply_negative_numbers(self):
        result = multiply_num(-3,-4)
        self.assertEqual(result,12)

    def test_multiply_with_zero(self):
        result = multiply_num(self.a,0)
        self.assertEqual(result,0)

    def tearDown(self):
        print("Cleaning up the test environment")
        del self.a
        del self.b


if __name__ == "__main__":
    unittest.main()




    
