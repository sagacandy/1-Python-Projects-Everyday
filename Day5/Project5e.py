import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

print("Welcome to the py password generator!")

l = int(input("How many letters would you like in your password? "))
s = int(input("How many symbols would you like? "))
n = int(input("How many numbers would you like? "))

password_list = []

# add random letters to password
for i in range(l):
    password_list.append(random.choice(alphabet))

# add random symbols to password
for i in range(s):
    password_list.append(random.choice(symbols))

# add random numbers to password
for i in range(n):
    password_list.append(random.choice(numbers))

# shuffle password list
random.shuffle(password_list)

# join password list into a single string
password = "".join(password_list)

print("Your password is: " + password)
