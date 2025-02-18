decimal, point = map(int, input().split("."))

n = decimal * 100 + point

print("NOTAS:")

notes = [100, 50, 20, 10, 5, 2]

for note in notes:
    print(f'{n // (note * 100)} nota(s) de R$ {note}.00')
    n %= note * 100

print("MOEDAS:")
coins = [100, 50, 25, 10, 5, 1]

for coin in coins:
    print(f'{n // coin} moeda(s) de R$ {coin / 100:.2f}')
    n %= coin
