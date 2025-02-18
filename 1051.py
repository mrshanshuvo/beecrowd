n = float(input())

if (0 <= n <= 2000):
    print("Isento")
elif (2000.01 <= n <= 3000):
    n -= 2000
    n = n*.08
    print(f'R$ {n:.2f}')
elif (3000.01 <= n <= 4500):
    n -= 2000
    n1 = n - 1000
    n -= n1
    n = (n1*0.18) + (n*0.08)
    print(f'R$ {n:.2f}')
else:
    n -= 2000

    n3 = n - 2500
    n -= n3
    n1 = n - 1500
    n -= n1

    result = n3*.28 + n*.18 + n1*.08

    print(f'R$ {result:.2f}')
