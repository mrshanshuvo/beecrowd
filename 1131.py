inter = gremio = empates = grenais = 0
while True:
    a, b = map(int, input().split())

    if (a > b):
        inter += 1
        grenais += 1
    elif (b > a):
        gremio += 1
        grenais += 1
    else:
        empates += 1
        grenais += 1

    n = int(input('Novo grenal (1-sim 2-nao)\n'))
    if (n == 2):
        break
print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')
if (inter == gremio):
    print(f'Não houve vencedor')
elif (inter > gremio):
    print(f'Inter venceu mais')
else:
    print(f'Gremio venceu mais')
