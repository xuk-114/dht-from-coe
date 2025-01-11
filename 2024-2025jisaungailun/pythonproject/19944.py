n = int(input())
for _ in range(n):
    a = list(map(int,input()))
    c = a[0]*10 + a[1]
    y = a[2]*10 + a[3]
    m = a[4]*10 + a[5]
    d = a[6]*10 + a[7]
    if m == 1:
        if y == 00:
            c = c - 1
            y = 99
        else:
            y = y - 1
        m = 13
    elif m == 2:
        if y == 00:
            c = c - 1
            y = 99
        else:
            y = y - 1
        m = 14
    w = (y + (y//4) + (c//4) - 2*c + (26*(m+1))//10 + d - 1) % 7
    if w == 0: print('Sunday')
    elif w == 1:print('Monday')
    elif w == 2:print('Tuesday')
    elif w == 3:print('Wednesday')
    elif w == 4:print('Thursday')
    elif w == 5:print('Friday')
    elif w == 6:print('Saturday')



