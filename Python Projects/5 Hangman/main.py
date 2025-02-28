import random
from words import words

def random_word():
    pass  # No need for this function right now

def play():
    words_history = []
    trials = 10
    word = random.choice(words)
    word_completion = list("_" * len(word))  # Convert to list for modification
    print(" ".join(word_completion))  # Display with spaces
    print("You are playing a Hangman game!")
    print(f"You have {trials} trials.")

    while trials > 0 and "_" in word_completion:
        letter = input("Enter a Letter: ").lower()

        if letter in words_history:
            print(f"You already guessed the letter '{letter}'.")
        else:
            words_history.append(letter)

            if letter in word:
                for i, char in enumerate(word):
                    if char == letter:
                        word_completion[i] = letter  # Replace "_" with the correct letter
                print(" ".join(word_completion))
            else:
                trials -= 1
                print(f"Incorrect! You have {trials} trials left.")

        if "_" not in word_completion:
            print(f"Congratulations! You guessed the word '{word}' 🎉")
            break

    if "_" in word_completion:
        print(f"Game Over! The correct word was '{word}'.")

random_word()
play()
