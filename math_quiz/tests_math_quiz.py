import unittest
from math_quiz import generate_random_integer, choose_random_operator, generate_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test that random numbers are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Run 1000 times to check for randomness
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)  # Assert number is within range

    def test_choose_random_operator(self):
        """Test that the operator is one of the expected options."""
        operators = ['+', '-', '*']
        for _ in range(1000):  # Run 1000 times to test randomness
            operator = choose_random_operator()
            self.assertIn(operator, operators)  # Assert the operator is valid

    def test_generate_problem_and_answer(self):
        """Test that the problem string and answer are correct for each operator."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),  # Test addition
            (5, 2, '-', '5 - 2', 3),  # Test subtraction
            (5, 2, '*', '5 * 2', 10),  # Test multiplication
            (1, 1, '+', '1 + 1', 2),  # Simple addition
            (10, 5, '-', '10 - 5', 5),  # Simple subtraction
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)  # Assert problem format is correct
            self.assertEqual(answer, expected_answer)  # Assert the correct answer is generated


if __name__ == "__main__":
    unittest.main()
