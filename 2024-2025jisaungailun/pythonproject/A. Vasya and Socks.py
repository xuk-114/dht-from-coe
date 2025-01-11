n,m = map(int,input().split())
day = 1
socks = n
while True:
    if socks < day:
        print(day-1)
        break
    if day % m == 0:
        socks += 1
    day += 1


