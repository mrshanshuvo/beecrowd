a, b, c = map(int, input().split())

if (a == 0):
    a = 24
    time = a + b + c
else:
    time = a + b + c

if (time >= 24):
    time -= 24

print(time)
