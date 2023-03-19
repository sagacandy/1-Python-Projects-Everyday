# FizzBuzz game range 1 to 100

list1 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list1.append("FizzBuzz")
    if i % 3 == 0:
        list1.append("Fizz")
    if i % 5 == 0:
        list1.append("Buzz")
    else:
        list1.append(i)
print(list1)


# OddEven version of FizzBuzz Game
l = []
for a in range(1, 11):
    if a % 2 == 0:
        l.append("Even")
    if a % 2 == 1:
        l.append("Odd")
    else:
        l.append(a)
print(l)
