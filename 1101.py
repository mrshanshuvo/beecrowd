while True:
    m, n = map(int, input().split())
    sum = 0
    if (m <= 0 or n <= 0):
        break
    elif (m < n):
        for i in range(m, n+1):
            print(i, end=' ')
            sum += i
        print(f'Sum={sum}')
    elif (m > n):
        for i in range(n, m+1):
            print(i, end=' ')
            sum += i
        print(f'Sum={sum}')
