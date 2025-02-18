n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

numbers = n1, n2, n3, n4, n5, n6
count = 0
positive = []
for number in numbers:
    if (number >= 0):
        count += 1
        positive.append(number)

avg = (sum(positive))/count
print(f'{count} valores positivos\n{avg:.1f}')
