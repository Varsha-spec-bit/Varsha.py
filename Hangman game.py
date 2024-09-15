import random

def choose_word():
    words = ['python', 'java', 'javascript', 'hangman', 'developer' ,'varsha','annaya']
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed = '_' * len(word)
    guessed_correctly = False
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print(guessed)

    while not guessed_correctly and wrong_guesses < max_wrong_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            guessed = ''.join([letter if letter == guess else guessed[i] for i, letter in enumerate(word)])
            print(guessed)
        else:
            wrong_guesses += 1
            print(f"Wrong guess! {max_wrong_guesses - wrong_guesses} attempts left.")

        if '_' not in guessed:
            guessed_correctly = True

    if guessed_correctly:
        print("Congratulations! You've guessed the word.")
    else:
        print(f"Sorry, you've been hanged! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
