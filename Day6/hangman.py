import random

# Define the word list and the hangman stages
word_list = ["aardvark", "baboon", "camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Select a random word and initialize the game state
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
chosen_word_list = list(chosen_word)

# Set the maximum number of incorrect guesses and initialize the incorrect guess counter
max_incorrect_guesses = len(stages) - 1
incorrect_guesses = 0

# Loop until the player wins or loses
while chosen_word_list != display and incorrect_guesses < max_incorrect_guesses:
    guess = input("Enter your guess letter: ").lower()
    if guess in chosen_word_list:
        for position in range(word_length):
            if chosen_word_list[position] == guess:
                display[position] = guess
    else:
        incorrect_guesses += 1
        print(stages[incorrect_guesses])
    print(display)

# Check if the player won or lost
if incorrect_guesses == max_incorrect_guesses:
    print("Game over. You ran out of lives. The word was", chosen_word)
else:
    print("Congratulations, you guessed the word!")
