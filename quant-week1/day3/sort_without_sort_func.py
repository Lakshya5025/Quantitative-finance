list = [1, 3,2, 5, 2, 9, 8, 49, 6]

length = len(list)
for i in range(length):
    for j in range(1, length - i -1  ):
        if(list[j] > list[j + 1]):
            list[j], list[j + 1] = list[j+ 1] , list[j]

print(list)