# Project c of Day 5 Adding Even Numbers

even_list = []
for i in range(1, 101):
    if i % 2 == 0:
        a = i
        even_list.append(a)
print(even_list)
print(sum(even_list))
