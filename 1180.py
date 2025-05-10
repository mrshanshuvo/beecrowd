n = int(input())
numbers = list(map(int, input().split()))

min_value = numbers[0]
min_position = 0

for i in range(1, n):
    if numbers[i] < min_value:
        min_value = numbers[i]
        min_position = i

print(f"Menor valor: {min_value}")
print(f"Posicao: {min_position}")
