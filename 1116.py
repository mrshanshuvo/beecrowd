N = int(input())

while (N > 0):
    a, b = map(int, input().split())
    if (a != 0 and b != 0):
        print(a/b)
    elif (a != 0 and b == 0):
        print("divisao impossivel")
    else:
        print(a/b)
    N -= 1
