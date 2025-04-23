N = []
for i in range(20):
    n = int(input())
    N.append(n)
j = 19
i = 0
while i < j:
    temp = N[i]
    N[i] = N[j]
    N[j] = temp
    j -= 1
    i += 1

for i in range(20):
    print(f'N[{i}] = {N[i]}')
