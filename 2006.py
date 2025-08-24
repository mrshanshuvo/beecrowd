t = int(input())

answers = list(map(int, input().split()))

count = 0

for answer in answers:
    if (answer == t):
        count += 1

print(count)
