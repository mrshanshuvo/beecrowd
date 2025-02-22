n = int(input())
c = r = s = total = 0
for i in range(n):
    a, t = map(str, input().split())
    a = int(a)

    if (t == 'C'):
        c += a
    elif (t == 'R'):
        r += a
    else:
        s += a

    total += a

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')

print(f'Percentual de coelhos: {((c/total)*100):.2f} %')
print(f'Percentual de ratos: {((r/total)*100):.2f} %')
print(f'Percentual de sapos: {((s/total)*100):.2f} %')
