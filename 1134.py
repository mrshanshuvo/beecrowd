alc = gas = die = 0
while True:
    n = int(input())
    if (n == 1):
        alc += 1
    elif (n == 2):
        gas += 1
    elif (n == 3):
        die += 1
    elif (n == 4):
        break

print("MUITO OBRIGADO")
print(f"Alcool: {alc}\nGasolina: {gas}\nDiesel: {die}")
