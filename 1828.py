n = int(input())
count = 1
for i in range(n):
    a, b = input().split()
    if a == b:
        print(f'Caso #{count}: De novo!')
    elif (a == 'tesoura' and b in ['papel', 'lagarto']) or \
         (a == 'papel' and b in ['pedra', 'Spock']) or \
         (a == 'pedra' and b in ['lagarto', 'tesoura']) or \
         (a == 'lagarto' and b in ['Spock', 'papel']) or \
         (a == 'Spock' and b in ['tesoura', 'pedra']):
        print(f'Caso #{count}: Bazinga!')
    else:
        print(f'Caso #{count}: Raj trapaceou!')
    count += 1
