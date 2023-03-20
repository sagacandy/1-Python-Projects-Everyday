import random

a = "abcdefghijklmopqrstuvwxyz"
n = "1234567890"
s = "!@#$%^&*()_+"

p_list = []

a1 = int(input("How many alphabets would you like in password: "))
n1 = int(input("How many numbers in your password: "))
s1 = int(input("How many symbolls in your password: "))

for a2 in range(a1):
    p_list.append(random.choice(a))
for n2 in range(n1):
    p_list.append(random.choice(n))
for s2 in range(s1):
    p_list.append(random.choice(s))
print(p_list)
nlist = random.shuffle(p_list)
print(nlist)
# p = "".join(nlist)
# print(p)

# print(len(nlist))
