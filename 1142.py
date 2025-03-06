n = int(input())
a = 1
for i in range(n):
    for j in range(4):
        if (a % 4 == 0):
            print("PUM", end="")
        else:
            print(a, end=" ")
        a += 1
    print()
