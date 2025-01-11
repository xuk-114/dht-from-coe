n = int(input())
id = []
for _ in range(n):
    a,b =map(str,input().split())
    b = int(b)
    id.append([b,a])
id_1 = id[:]
id_1.sort(key=lambda x: (-x[0],id.index(x)))
for i in range(n):
    if id_1[i][0]>= 60 :
        print(id_1[i][1])
for i in id:
    if i[0] <60:
        print(i[1])