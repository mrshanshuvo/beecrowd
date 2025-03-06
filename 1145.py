a, b = map(int, input().split())
count = 0
for i in range(1, b + 1):
    if count == a:
        print()
        count = 0
    if count > 0:
        print(" ", end="")
    print(i, end="")
    count += 1
if count > 0:
    print()
