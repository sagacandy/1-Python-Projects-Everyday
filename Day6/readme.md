# Hangman Game in Python

In this code, we added the stages list containing the ASCII art for the hangman stages. We also set the maximum number of incorrect guesses allowed to be the length of the stages list minus 1, which corresponds to the number of stages available.

We then added a counter incorrect_guesses to keep track of the number of incorrect guesses made by the player. Inside the game loop, if the player makes an incorrect guess, we increment the incorrect_guesses counter and print the corresponding hangman stage. We also added a check to see if the player ran out of lives, and if so, we print a game over message and reveal the chosen word. If the player correctly guesses all the letters in the chosen word before running out of lives, we print a congratulations message.
