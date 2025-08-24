n = int(input())

for i in range(n):
    name, force = map(str, input().split())
    force = int(force)
    if (name == 'Thor'):
        print('Y')
    else:
        print('N')
