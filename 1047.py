start_hr, start_min, final_hr, final_min = map(int, input().split())

start_min_total = start_hr * 60 + start_min
final_min_total = final_hr * 60 + final_min

if (start_min_total < final_min_total):
    total_mins = final_min_total - start_min_total

else:
    total_mins = (24 * 60 - start_min_total) + final_min_total

hour = total_mins//60
min = total_mins % 60

print(f"O JOGO DUROU {hour} HORA(S) E {min} MINUTO(S)")
