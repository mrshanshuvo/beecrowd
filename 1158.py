n = int(input())
numbers = []
for i in range(n):
    x, y = map(int, input().split())
    if (x % 2 == 0):
        x += 1
        for i in range(y):
            if (x % 2 == 1):
                numbers.append(x)
                x += 2
    else:
        for i in range(y):
            if (x % 2 == 1):
                numbers.append(x)
                x += 2

    print(sum(numbers))
    numbers = []
