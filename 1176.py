fibo = [0, 1]
for i in range(61):
    sum = fibo[i] + fibo[i+1]
    fibo.append(sum)

t = int(input())
count = 0
while (count != t):
    n = int(input())
    count += 1
    print(f'Fib({n}) = {fibo[n]}')
