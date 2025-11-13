import random

# Predefined list of words
words = ["apple", "banana", "orange", "grape", "melon"]

# Choose a random word
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
wrong_guesses = []
max_attempts = 6
attempts = 0

print("=== Welcome to Hangman! ===")

# Game loop
while attempts < max_attempts and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print(f"Wrong guesses ({attempts}/{max_attempts}):", " ".join(wrong_guesses))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_word or guess in wrong_guesses:
        print("You already guessed that letter!")
        continue

    if guess in secret_word:
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess
        print("Good guess!")
    else:
        wrong_guesses.append(guess)
        attempts += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n😢 Game Over! The correct word was:", secret_word)
