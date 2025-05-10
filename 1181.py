L = int(input())
T = input()
M = []
for i in range(12):
    row = []
    for j in range(12):
        n = float(input())
        row.append(n)
    M.append(row)


eLements = M[L]
summation = sum(eLements)
if (T == 'S'):
    print(f'{summation:.1f}')
if (T == 'M'):
    avg = summation/12
    print(f'{avg:.1f}')
