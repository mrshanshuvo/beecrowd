while True:
    n = int(input())
    speeds = list(map(int, input().split()))

    max_speed = max(speeds)

    if max_speed < 10:
        print(1)
    elif 10 <= max_speed < 20:
        print(2)
    else:
        print(3)
