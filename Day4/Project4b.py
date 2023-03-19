# Roulette Who will pay the bill
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_names = len(names)
random_name_number = random.randint(0, num_of_names-1)
random_name = names[random_name_number]
print(f"{random_name} is going to buy the meal today!")
