n = int(input())
in_interval = 0
out_interval = 0
for i in range(n):
    x = int(input())
    if (10 <= x <= 20):
        in_interval += 1
    else:
        out_interval += 1

print(f'{in_interval} in\n{out_interval} out')
