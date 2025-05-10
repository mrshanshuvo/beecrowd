C = int(input())
T = input()
M = []
for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    M.append(row)

col_numbers = []
for i in range(12):
    col_numbers.append(M[i][C])

summation = sum(col_numbers)
if (T == 'S'):
    print(f'{summation:.1f}')
if (T == 'M'):
    avg = summation/12
    print(f'{avg:.1f}')
