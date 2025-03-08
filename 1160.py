t = int(input())

for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())

    pa, pb = int(pa), int(pb)

    count = 0
    while pa <= pb and count <= 100:
        pa += int(pa * g1/100)
        pb += int(pb * g2/100)
        count += 1

    if (count > 100):
        print("Mais de 1 seculo.")
    else:
        print(f'{count} anos.')
