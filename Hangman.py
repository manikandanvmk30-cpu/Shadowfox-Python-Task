import random

def choose_word():
    words = ["python", "developer", "hangman", "variable", "function", "loop", "debug"]
    return random.choice(words)

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """
    ]
    return stages[6 - attempts]

def play_game():
    word = choose_word()
    guessed_letters = []
    correct_letters = ["_"] * len(word)
    attempts = 6

    print("🎮 Welcome to Hangman!")
    while attempts > 0 and "_" in correct_letters:
        print(display_hangman(attempts))
        print("Word:", " ".join(correct_letters))
        print("Guessed letters:", " ".join(guessed_letters))

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Enter a single alphabet.")
            continue
        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    correct_letters[i] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print("❌ Wrong!")

    if "_" not in correct_letters:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(attempts))
        print("💀 Game Over. The word was:", word)

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
