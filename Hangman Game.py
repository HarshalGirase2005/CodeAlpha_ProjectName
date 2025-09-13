#Hangman Game...
import random

def hangman():
    # Predefined list of words
    words = ["python", "hangman", "coding", "developer", "program"]
    word = random.choice(words)  # Pick a random word
    
    guessed_word = ["_"] * len(word)  # Display underscores for unguessed letters
    guessed_letters = []  # Keep track of guessed letters
    attempts = 6  # Max incorrect guesses allowed

    print("Welcome to Hangman! 🎮")
    print("You have 6 incorrect guesses. Let's begin!\n")

    while attempts > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", guessed_letters)
        print(f"Remaining attempts: {attempts}")

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Wrong guess!\n")
            attempts -= 1

    # End of game
    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("😢 Out of attempts! The word was:", word)

# Run the game
hangman()
