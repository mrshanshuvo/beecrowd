numbers = []
for i in range(100):
    number = int(input())
    numbers.append(number)
max = 0
index = 0
count = 0
for number in numbers:
    count += 1
    if (max < number):
        max = number
        index = count

print(f'{max}\n{index}')
