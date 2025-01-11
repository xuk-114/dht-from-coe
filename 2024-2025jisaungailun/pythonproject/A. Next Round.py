n,k = map(int,input().split())
a = list(map(int,input().split()))
c = a[k-1]
d = 0
for num in a:
    if num > 0:
        if num >= c:
            d += 1

print(d)