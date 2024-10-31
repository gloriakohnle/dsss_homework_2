import random


def random_number(lower_limit: float, upper_limit: float) -> float:
    """ Generate random integer value in range (min, max) including limits min and max.

    Args:
        min (float): Minimum integer value in given range (including)
        max (float): Maximum integer value in given range (including)

    Returns:
        float: Integer value in range (min, max) including limits min and max
    """
    if lower_limit is not int or upper_limit is not int:
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
    return random.randint(lower_limit, upper_limit)


def random_operator() -> str:
    """ Randomly choose arithmetic operator from list (addition, subtraction, multiplication) as string value.

    Returns:
        str: String representing arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def calculate_two_numbers(number_1: float, number_2: float, operator: str) -> tuple[str, float]:
    """ Calculation of two numbers n1 and n2 based on input arithmetic operator o (addition, subtraction or multiplication).

    Args:
        n1 (float): Integer value that is used for calculation
        n2 (float): Integer value that is used for calculation
        o (str): String value representing arithmetic operator

    Returns:
        tuple[str, float]: Tuple of string value (arithmetic calculation) and integer value (result of mathematic operation)
    """
    calculation = f"{number_1} {operator} {number_2}"
    if operator == '+': result = number_1 + number_2
    elif operator == '-': result = number_1 - number_2
    else: result = number_1 * number_2
    return calculation, result

def math_quiz():
    count = 0
    game_length = int(input("How often do you want to play?"))

    #pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(game_length):
        number_1 = random_number(1, 10); 
        number_2 = random_number(1, 5.5); 
        operator = random_operator()

        PROBLEM, ANSWER = calculate_two_numbers(number_1=number_1, number_2=number_2, operator=operator)
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            count += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {count}/{game_length}")

if __name__ == "__main__":
    math_quiz()
