import math
s = 0
while True:
    flag = True
    cnt = 0
    try:
        n,d =map(int,input().split())
    except ValueError:
        continue
    s += 1
    if n==d==0: break
    lit = []
    for i in range(n):
        lit.append([ int(i) for i in input().split()])
    for i in range(n):
        if lit[i][1] > d:
            print(f'Case {s}: -1')
            flag = False
        for j in range(n-1-i):
            if lit[j][0] > lit[j+1][0]:
                lit[j][0],lit[j + 1][0] = lit[j+1][0],lit[j][0]
    for i in range(n):
        for j in range(n-1-i):
            if lit[j][0] == lit[j+1][0]:
                if lit[j][1] < lit[j+1][1]:
                    lit[j][1],lit[j+1][1] = lit[j+1][1],lit[j][1]
    if flag:
        x = float('inf')
        for i in range(n):
            if math.sqrt(abs(x-lit[i][0])**2 + lit[i][1]**2) <= d:
                continue
            x = lit[i][0]+math.sqrt(d**2-lit[i][1]**2)
            cnt +=1
        print(f'Case {s}: {cnt}')
