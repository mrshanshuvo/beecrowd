n = int(input())

for i in range(n):
    x = int(input())
    count = 0
    for i in range(1, x+1):
        if (x % i == 0):
            count += 1

    if count == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')
