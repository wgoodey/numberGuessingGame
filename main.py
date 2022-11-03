from random import randint

EASY_MODE = 10
HARD_MODE = 5


def set_difficulty():
    """Sets number of user guesses."""
    mode = input("Type \'hard\' for hard mode or anything for easy mode: ").lower()
    if mode == "hard":
        return HARD_MODE
    else:
        return EASY_MODE


def get_guess():
    """Asks user for a guess and returns their number if it's valid."""
    guess = 0
    valid = False
    while not valid:
        try:
            guess = int(input("Make a guess: "))
            if guess < 0 or guess > 100:
                print("Please pick a number between 1 and 100.")
            else:
                valid = True
        except ValueError:
            print("not a valid number.")
    return guess


def check_answer(guess, answer):
    """Checks answer against guess and prints a hint for the next guess, if any remain."""
    if guess == answer:
        print("You guessed the correct number!")
    elif num_guesses == 0:
        print(f"The number was {answer}")
    elif guess > answer:
        print(f"{user_guess} is too high.")
    else:
        print(f"{user_guess} is too low.")


def check_if_game_over():
    """Returns true if user guessed the number or ran out of guesses."""
    if user_guess == number or num_guesses == 0:
        return True
    return False


number = randint(1, 100)
print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.\n")
# print(f"pssst - it's {number}.")

num_guesses = set_difficulty()

game_over = False
while not game_over:
    if num_guesses == 1:
        print(f"This is your last guess!\n")
    else:
        print(f"You have {num_guesses} attempts to guess the number.\n")

    user_guess = get_guess()
    num_guesses -= 1
    check_answer(user_guess, number)
    game_over = check_if_game_over()
