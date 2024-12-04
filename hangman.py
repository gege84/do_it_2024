import random


def hangman_game():
    # List of words to choose from
    word_list = [
        "burti",
        "nemsi",
        "magida",
        "skami",
        "televizori",
        "karada",
        "cigni",
        "rveuli",
    ]

    # Randomly select a word from the list
    word = random.choice(word_list)

    # Create a list with underscores for each letter in the word
    hidden_word = ["_"] * len(word)

    # Set the number of allowed incorrect attempts
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    # Main game loop
    while attempts > 0:
        print("\nWord to guess:", " ".join(hidden_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"You have {attempts} attempts remaining.")

        # Get the user's guess
        guess = input("Guess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")

            # Update the hidden word with the correct guess
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess

            # Check if the word is completely guessed
            if "_" not in hidden_word:
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            attempts -= 1

    # If no attempts left, the game is over
    if attempts == 0:
        print(f"\nGame over! The word was: {word}")


# # Start the game
