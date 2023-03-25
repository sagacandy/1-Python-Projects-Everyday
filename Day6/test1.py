import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

# for c in chosen_word:
#     if guess in c:
#         print("True")
#     else:
#         print("False")

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ["_"]*(len(chosen_word))
print(display)
# n = len(chosen_word)
# for i in range(len(chosen_word)):
#     display.append("_")
# print(display)

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for p in range(len(chosen_word)):
    if guess == p:
        display.pop(p)
        display.insert(p, guess)
    # else:
    #     display.append("_")
print(display)
