a, b, c = map(float, input().split())
is_possible = False
if ((a < b+c) and (b < a+c) and (c < a+b)):
    is_possible = True

if (is_possible == True):
    print("Perimetro =", a+b+c)
else:
    area = 0.5 * (a + b) * c
    print("Area =", area)
