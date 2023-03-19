import random

# Define the hands
hands = ['rock', 'paper', 'scissors']

while True:
    # Get the player's hand
    player_hand = input("Enter your hand (rock, paper, or scissors): ").lower()

    # Validate the player's hand
    if player_hand not in hands:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    # Get the computer's hand
    computer_hand = random.choice(hands)

    # Print the hands
    print("You:", player_hand)
    print("Computer:", computer_hand)

    # Determine the winner
    if player_hand == computer_hand:
        print("It's a tie!")
    elif (player_hand == 'rock' and computer_hand == 'scissors') or \
         (player_hand == 'paper' and computer_hand == 'rock') or \
         (player_hand == 'scissors' and computer_hand == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask if the player wants to play again
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break
