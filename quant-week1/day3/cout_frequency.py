list = [1, 3, 5, 2, 5, 2, 6, 4, 4, 3, 2,0]
dict = {}

for i in list:
    if(dict.get(i)): dict[i] += 1
    else: dict[i] = 1

print(dict)