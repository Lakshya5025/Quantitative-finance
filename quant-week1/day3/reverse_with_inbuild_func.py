list = [1, 2, 3, 3, 4, 5, 2, 1, 6, 8]

start = 0
end = len(list) - 1

while(start < end):
    list[start], list[end] = list[end], list[start]
    start += 1
    end -= 1
print(list)