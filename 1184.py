M = []
T = input()
for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    M.append(row)

index = 0
lower_elements = []
for row in M:
    for i in range(12):
        if (i < index):
            lower_elements.append(row[i])
    index += 1

summation = sum(lower_elements)
total_elements = len(lower_elements)
if (T == 'S'):
    print(f'{summation:.1f}')
if (T == 'M'):
    avg = summation/total_elements
    print(f'{avg:.1f}')
