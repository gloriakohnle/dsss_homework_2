import random


def random_number(lower_limit: int, upper_limit: int) -> int:
    """ Generate random integer value in range (min, max) including limits min and max.

    Args:
        min (int): Minimum integer value in given range (including)
        max (int): Maximum integer value in given range (including)

    Returns:
        int: Integer value in range (min, max) including limits min and max
    """
    try:
        return random.randint(lower_limit, upper_limit)
    except ValueError:
        print("Invalid arguments: Arguments have to be integer values")


def random_operator() -> str:
    """ Randomly choose arithmetic operator from list (addition, subtraction, multiplication) as string value.

    Returns:
        str: String representing arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def calculate_two_numbers(number_1: int, number_2: int, operator: str) -> tuple[str, int]:
    """ Calculation of two numbers n1 and n2 based on input arithmetic operator (addition, subtraction or multiplication).

    Args:
        number_1 (int): Integer value that is used for calculation
        number_2 (int): Integer value that is used for calculation
        operator (str): String value representing arithmetic operator

    Returns:
        tuple[str, int]: Tuple of string value (arithmetic calculation) and integer value (result of mathematic operation)
    """
    # store calculation as string value for display:
    calculation = f"{number_1} {operator} {number_2}"
    # calculate based on input operator:
    if operator == '+': result = number_1 + number_2
    elif operator == '-': result = number_1 - number_2
    else: result = number_1 * number_2 # else: '*' operator
    return calculation, result

def math_quiz():
    """ Math quiz that randomly presents arithmetic calculations (addition, subtraction, multiplication) of two integer numbers
        and gives feedback to the user whether the input result by the user is correct or not.
    """
    # count is amount of correct answers by the user (score)
    count = 0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    try:
        game_length = int(input("How often do you want to play?"))
    except ValueError:
        print("User Input is not an integer!")

    # iterate to present as many calculations as indicated by the user previously
    for _ in range(game_length):
        number_1 = random_number(1, 10); # random number in the range of 1 and 10 (including)
        number_2 = random_number(1, 6); # random number in the range of 1 and 6 (including)
        operator = random_operator() # random operator (addition, subtraction or multiplication)

        # calculation part
        PROBLEM, CORRECT_ANSWER = calculate_two_numbers(number_1=number_1, number_2=number_2, operator=operator)
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")

        # throw ValueError if user input is not integer value:
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("User Input is not an integer!")

        if user_answer == CORRECT_ANSWER:
            print("Correct! You earned a point.")
            # increase user's score by one
            count += 1
        else:
            print(f"Wrong answer. The correct answer is {CORRECT_ANSWER}.")

    print(f"\nGame over! Your score is: {count}/{game_length}")

if __name__ == "__main__":
    math_quiz()
