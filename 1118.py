def check_validity(a):
    if (0 <= a <= 10):
        return a
    else:
        print("nota invalida")
        return None


x = 1
while x == 1:
    while True:
        a = check_validity(float(input()))
        if a is not None:
            break

    while True:
        b = check_validity(float(input()))
        if b is not None:
            break

    media = (a+b)/2
    print(f'media = {media:.2f}')

    while True:
        x = int(input("novo calculo (1-sim 2-nao)\n"))

        if x in [1, 2]:
            break

    if (x == 2):
        break
