import math
while True:
    n = int(input())
    if n == 0:
        break
    time_2 = float('inf')
    for _ in range(n):
        speed,time = map(int,input().split())
        if time < 0:
            continue
        time_1 =math.ceil((4.5/speed)*3600 + time)
        time_2 = min(time_1,time_2)
    print(time_2)