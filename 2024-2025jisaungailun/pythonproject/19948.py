n,m = map(int,input().split())
rank = list(map(int,input().split()))
s = []
rank.sort()
for i in range(1,n):
    s.append(rank[i]-rank[i-1])
s.sort(reverse=True)
d = sum(s)
for i in range(m-1):
    d -= s[i]
print(d)