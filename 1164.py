n = int(input())

for i in range(n):
    divisors = []
    x = int(input())
    for i in range(1, int(x/2)+1):
        if (x % i == 0):
            divisors.append(i)
    if sum(divisors) == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
