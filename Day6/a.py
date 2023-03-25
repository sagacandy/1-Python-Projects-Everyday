import random
word_list = ["aardvark", "baboon", "camel"]

# task1
chosen_word = random.choice(word_list)
print(chosen_word)
# guess = input("Enter the your guess letter: ").lower()
# for c in chosen_word:
#     if guess == c:
#         print("True")
#     else:
#         print("False")


# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ["_"]*len(chosen_word)
print(display)
