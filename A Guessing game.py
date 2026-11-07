
import random

words = ["python", "computer", "programming", "science", "keyboard"]

secret_word = random.choice(words)
guess_count = 0
guess_limit = 3
won = False

print("Welcome to the Word Guessing Game!")
print("You have 3 attempts to guess the secret word.")

while guess_count < guess_limit:
    guess = input("Enter your guess: ").strip().lower()
    guess_count += 1

    if guess == secret_word:
        won = True
        print("Congratulations! YOU WIN!")
        break

    else:
        print("Wrong guess!")

        if guess_count == 1:
            print("HINT: The word has", len(secret_word), "letters.")

        elif guess_count == 2:
            print("HINT: The word starts with", secret_word[0].upper())

        else:
            print("Out of attempts! YOU LOSE!")
            print("The secret word was:", secret_word)

