n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
total = 0
for i in range(m):
    if a[i] >= 0 :
        break
    total += a[i]
print(-total)

