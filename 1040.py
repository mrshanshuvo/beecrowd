inputs = list(map(float, input().split()))
a, b, c, d = inputs
avg = (a*2 + b*3 + c*4 + d*1)/10
print(f"Media: {avg:.1f}")
if (avg >= 7.0):
    print("Aluno aprovado.")
elif (avg < 5.0):
    print("Aluno reprovado.")
elif (avg >= 5 and avg <= 6.9):
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")

    new_avg = (avg + e)/2

    if (new_avg >= 5):
        print("Aluno aprovado.")
    elif (new_avg <= 4.9):
        print("Aluno reprovado.")

    print(f"Media final: {new_avg:.1f}")
