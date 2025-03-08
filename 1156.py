s = 0
j = 1
for i in range(1, 40, 2):
    s += (i/j)
    # print(f"{i}/{j}")
    j *= 2

print(f'{s:.2f}')
