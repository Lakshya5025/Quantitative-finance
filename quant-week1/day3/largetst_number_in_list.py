list = [1, 2, 5, 2, 1, 66, 34, 64, 3, 5432, 5, 32,46, 324]

largest = list[0]
for i in list:
    if(i  > largest): largest = i
print(largest)