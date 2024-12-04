import random


def guess_the_number_game():
    print("Welcome to 'Guess the Number'!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    # დააგენერირე რიცხვი  1 დან 100-მდე
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # მიეცი ადამიანს გამოცნობის საშუალება
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            # If the user doesn't enter a valid number
            print("Please enter a valid number.")
            continue

        # Increase the attempt count
        attempts += 1

        # Check if the guess is correct
        if user_guess < secret_number:
            print("Your guess is too low! Try a higher number.")
        elif user_guess > secret_number:
            print("Your guess is too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number}.")
            print(f"It took you {attempts} attempts.")
            break


# # Start the game
guess_the_number_game()
