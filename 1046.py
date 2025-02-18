start, end = map(int, input().split())
time = 0

if (start > end):
    time = (24 - start) + end
elif (start == end):
    time = 24
else:
    time = end - start

print(f'O JOGO DUROU {time} HORA(S)')
