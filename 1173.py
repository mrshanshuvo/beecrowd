n = int(input())
numbers = []
for i in range(10):
    numbers.append(n)
    n *= 2

for i in range(10):
    print(f'N[{i}] = {numbers[i]}')
