print('''Welcome to Treasure Island.
Your mission is to find the treasure.
''')
path1 = input(
    'You\'re at a crossroad, where do you want to go? Type "Left" or "Right".').lower()
if path1 == "left":
    path2 = input(
        'You\'ve come to the lake. There is an island in the middle of lake. Type "wait" for boat or "swim" to swim to the lake.').lower()
    if path2 == "wait":
        path3 = input(
            'You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()
        if path3 == "red":
            print("Burned by fire. Game Over!!")
        elif path3 == "blue":
            print("Eaten by Beats. Game Over!!")
        elif path3 == "yellow":
            print("You win")
        else:
            print("Game Over!!!")
    else:
        print("You are attacked by trout. Game Over!!")
else:
    print("You fell into the hole Game Over!!")
