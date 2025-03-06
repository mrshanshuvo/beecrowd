values = list(map(int, input().split()))
a = values[0]

for value in values[1:]:
    if (value > 0):
        n = value

numbers = []
for i in range(n):
    numbers.append(a)
    a += 1

print(sum(numbers))
