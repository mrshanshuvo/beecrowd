x = int(input())
y = int(input())

odd_numbers = []
if (x < y):
    for i in range(x+1, y):
        if (i % 2 != 0):
            odd_numbers.append(i)
elif (x > y):
    temp = x
    x = y
    y = temp
    for i in range(x+1, y):
        if (i % 2 != 0):
            odd_numbers.append(i)
else:
    odd_numbers.append(0)

print(sum(odd_numbers))
