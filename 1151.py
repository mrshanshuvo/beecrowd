n = int(input())
fibos = [0, 1]

for i in range(n-2):
    fibos.append(fibos[i]+fibos[i+1])

for i in range(n):
    if (i == n-1):
        print(fibos[i])
    else:
        print(fibos[i], end=" ")
