n = int(input())
a = []
for i in range(n):
    compete,write = map(int,input().split())
    a.append([compete,write])
a.sort(key = lambda x: (x[0],x[1]))
time = a[0][0] - 1
for j in range(1,n):
    write = a[j-1][1]
    compete = a[j][0]
    time += max(compete,write)
time += a[-1][1]
print(time)