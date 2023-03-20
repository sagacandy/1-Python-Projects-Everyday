# Project a of Day 5
# we are finding the average height of students without using sum() and len() function and understanding how those functions work at under the hood.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Understanding the sum() under the hood
gtotal = 0
for total in student_heights:
    gtotal = gtotal+total

# understanding the len() function under the hood
glenth = 0
for l in student_heights:
    glenth = glenth+1

# find the average
average_height = round(gtotal/glenth)
print(average_height)
