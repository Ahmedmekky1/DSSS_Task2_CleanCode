import random

def generate_random_integer(min_val: int, max_val: int) -> int:
    """Generate a random integer between min_val and max_val inclusive."""
    return random.randint(min_val, max_val)

def choose_random_operator() -> str:
    """Randomly choose an operator from addition, subtraction, or multiplication."""
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer(num1: int, num2: int, operator: str) -> tuple[str, int]:
    """
    Generate a math problem string and its correct answer based on the operator.

    Args:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The operator to apply (+, -, *).

    Returns:
        tuple[str, int]: A tuple containing the problem as a string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem, answer

def math_quiz(total_questions: int = 3) -> None:
    """
    Run a math quiz game where the user answers random math problems.

    Args:
        total_questions (int): Number of questions in the quiz.
    """
    score = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Using an integer range
        operator = choose_random_operator()

        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
