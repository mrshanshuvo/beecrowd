n = int(input())
weights = []
for i in range(n):
    a, b, c = map(float, input().split())
    weighted_avg = (a*2 + b*3 + c*5)/10
    weights.append(weighted_avg)

for i in weights:
    print(f'{i:.1f}')
