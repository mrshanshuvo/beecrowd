while True:
    x = int(input())
    if (x == 0):
        break
    sum = 0
    if x % 2 != 0:
        x += 1
    for i in range(5):
        sum += x
        x += 2
    print(sum)
