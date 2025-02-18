s_day = input()
s_day = int(s_day.split()[1])
s_hr, s_min, s_sec = map(int, input().split(":"))

e_day = input()
e_day = int(e_day.split()[1])
e_hr, e_min, e_sec = map(int, input().split(":"))

total_end_sec = (e_day * 86400) + (e_hr * 3600) + (e_min * 60) + e_sec
total_start_sec = (s_day * 86400) + (s_hr * 3600) + (s_min * 60) + s_sec

event_time = total_end_sec - total_start_sec

day = event_time // 86400
rem = event_time % 86400

hour = rem // 3600
rem = rem % 3600

min = rem // 60
sec = rem % 60

print(f'{day} dia(s)\n{hour} hora(s)\n{min} minuto(s)\n{sec} segundo(s)')
