while (True):
    a = float(input())
    if (0 <= a <= 10):
        break
    print("nota invalida")

while (True):
    b = float(input())
    if (0 <= b <= 10):
        break
    print("nota invalida")

avg = (a + b)/2

print(f"media = {avg:.2f}")
