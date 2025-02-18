salary = float(input())

if (0 <= salary <= 400):
    earned = salary * 0.15
    salary = salary + earned
    percentage = 15

elif (400 < salary <= 800):
    earned = salary * 0.12
    salary = salary + earned
    percentage = 12

elif (800 < salary <= 1200):
    earned = salary * 0.10
    salary = salary + earned
    percentage = 10

elif (1200 < salary <= 2000):
    earned = salary * 0.07
    salary = salary + earned
    percentage = 7

else:
    earned = salary * 0.04
    salary = salary + earned
    percentage = 4

print(f'Novo salario: {salary:.2f}')
print(f'Reajuste ganho: {earned:.2f}')
print(f'Em percentual: {percentage} %')
