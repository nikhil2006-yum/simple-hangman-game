import random

# List of words to choose from
word_list = ['python', 'hangman', 'computer', 'science', 'keyboard']

# Randomly choose a word
word = random.choice(word_list)
word_letters = list(word)  # Turn the word into a list of characters
guessed_letters = ['_'] * len(word)  # Displayed version of word
attempts = 6  # Number of incorrect guesses allowed

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Main game loop
while attempts > 0 and '_' in guessed_letters:
    print("\nWord: ", ' '.join(guessed_letters))
    print("Remaining attempts:", attempts)
    
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single alphabet.")
        continue

    if guess in word_letters:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# End of game
if '_' not in guessed_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over! The word was:", word)
