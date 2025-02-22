i = 0
while i <= 2:
    for j in range(1, 4):
        if ((i == 0) or (i == 1) or (i == 2)):
            print(f"I={int(i)} J={int(i+j)}")
        else:
            print(f"I={i:.1f} J={i+j:.1f}")
    i += 0.2
    i = float(f'{i:.2f}')
