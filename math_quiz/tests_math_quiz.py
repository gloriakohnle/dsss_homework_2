import unittest
from math_quiz import random_number, random_operator, calculate_two_numbers


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        """ Test if random numbers generated are within the specified range
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        """ Test if random operator generated is one of the specified list
        """
        for _ in range(1000): # Test a large number of random operators
            rand = random_operator()
            self.assertTrue(rand == '+' or rand == '-' or rand == '*')

    def test_calculate_two_numbers(self):
        """ Test if generated problem and result are correct
        """
        # Manually defined test cases (ground truth data)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (4, 1, '-', '4 - 1', 3),
            (8, 3, '*', '8 * 3', 24),
            (1, 6, '-', '1 - 6', -5),
            (2, 9, '+', '2 + 9', 11),
            (5, 9, '*', '5 * 9', 45)
        ]

        # Test for all entries in test_cases array
        for num1, num2, operator, expected_problem, expected_answer in test_cases: 
            self.assertTrue(calculate_two_numbers(num1, num2, operator) == (expected_problem, expected_answer))

if __name__ == "__main__":
    unittest.main()
