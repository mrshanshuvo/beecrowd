n = int(input())

for i in range(1, 10001):
    if (i == 2):
        print(i)
    elif (i % n == 0):
        print(i+2)
