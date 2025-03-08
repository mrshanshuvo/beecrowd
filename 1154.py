numbers = []
while True:
    n = int(input())

    if (n < 0):
        break

    numbers.append(n)

count = len(numbers)

avg = (sum(numbers))/count

print(f'{avg:.2f}')
