import random
import module
import words

print(module.hangman)
words.words  # module defined in words.py

# Select a random word and initialize the game state
chosen_word = random.choice(words.words)
words.words = len(chosen_word)
display = ["_"] * words.words
chosen_word_list = list(chosen_word)

# Set the maximum number of incorrect guesses and initialize the incorrect guess counter
max_incorrect_guesses = len(module.stages) - 1
incorrect_guesses = 0

# Loop until the player wins or loses
while chosen_word_list != display and incorrect_guesses < max_incorrect_guesses:
    guess = input("Enter your guess letter: ").lower()
    if guess in chosen_word_list:
        for position in range(words.words):
            if chosen_word_list[position] == guess:
                display[position] = guess
    else:
        incorrect_guesses += 1
        print(module.stages[incorrect_guesses])
    print(display)
# Check if the player won or lost
if incorrect_guesses == max_incorrect_guesses:
    print("Game over. You ran out of lives. The word was", chosen_word)
else:
    print("Congratulations, you guessed the word!")
