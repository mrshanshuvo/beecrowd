while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break

    if m == 0 and n == 0:
        fact = 2
    elif m == 0:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        fact += 1
    elif n == 0:
        fact = 1
        for i in range(1, m + 1):
            fact *= i
        fact += 1
    else:
        fact_m = 1
        for i in range(1, m + 1):
            fact_m *= i
        fact_n = 1
        for i in range(1, n + 1):
            fact_n *= i
        fact = fact_m + fact_n

    print(fact)
