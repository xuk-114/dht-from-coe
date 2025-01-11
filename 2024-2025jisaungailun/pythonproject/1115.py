def stone(a,b,t):
    global mar
    if b == 0:
        return
    if a/b >= 2:
        mar.append(t)
    else:
        stone(b,a-b,t+1)
while True:
    mar = []
    m,n =map(int,input().split())
    s = max(m,n)
    q = min(m,n)
    stone(s,q,1)
    if m==n==0:
        break
    if m == n:
        print('win')
        continue
    ans = max(mar)
    if ans % 2 == 0:
        print('lose')
    else :
        print('win')

