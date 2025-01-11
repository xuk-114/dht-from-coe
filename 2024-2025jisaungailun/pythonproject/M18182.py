p = int(input())
for _ in range(p):
    ans = 0
    time = -1
    n, m, b = map(int, input().split())
    z = []
    for _ in range(n):
        t,x=map(int,input().split())
        z.append([t,x])
    z.sort(key = lambda x: (x[0],-x[1]))
    cnt = 1
    t = z[0][0]
    for i in z:
        if t == i[0]:
            if cnt <= m:
                ans+=i[1]
                if ans >=b:
                    time = i[0]
                    break
            cnt += 1
        else:
            cnt = 2
            ans+=i[1]
            if ans>=b:
                time = i [0]
                break
        t = i[0]
    if ans>=b:
        print(time)
    else :
        print('alive')