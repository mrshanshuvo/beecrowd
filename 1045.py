numbers = list(map(float, input().split()))

numbers.sort(reverse=True)

a, b, c = numbers

if (a >= (b+c)):
    print("NAO FORMA TRIANGULO")
else:
    if ((a*a) == (b*b + c*c)):
        print("TRIANGULO RETANGULO")

    if ((a*a) > (b*b + c*c)):
        print("TRIANGULO OBTUSANGULO")

    if ((a*a) < (b*b + c*c)):
        print("TRIANGULO ACUTANGULO")

    if (a == b == c):
        print("TRIANGULO EQUILATERO")

    if ((a == b != c) or a != b == c):
        print("TRIANGULO ISOSCELES")
