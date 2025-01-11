n,m_1,m_2 = map(int,input().split())
x = []
y = []
z = []
for _ in range(m_1):
    p = input().split()
    x.append((int(p[0]),int(p[1]),int(p[2])))
for _ in range(m_2):
    p = input().split()
    y.append((int(p[0]), int(p[1]), int(p[2])))
for i in range(n):#row
    for j in range(n):#col
        ans = 0
        for l in y:
            if l[1]==j:
                for m in x :
                    if m[0] == i and m[1]==l[0]:
                        ans += l[2]*m[2]
        if ans !=0:
            z.append((i,j,ans))
for a,b,c in z:
    print(a,b,c)

