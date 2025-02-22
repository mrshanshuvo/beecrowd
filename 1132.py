a = int(input())
b = int(input())
sum = 0
if (a < b):
    while (a <= b):
        if (a % 13 != 0):
            sum += a
        a += 1

if (b < a):
    while (b <= a):
        if (b % 13 != 0):
            sum += b
        b += 1

print(sum)
