n,d = map(int,input().split())
h = [int(input()) for _ in range(n)]
num = []
inf = int(1e9)
used = [0] * n
for _ in range(n):
    minv,maxv = inf,-inf
    idx ,val = 0 ,inf
    for i in range(n):
        if used[i]:
            continue
        minv = min(minv,h[i])
        maxv = max(maxv,h[i])
        if (h[i] + d >= maxv and h[i] -d <= minv and h[i] <val):
            val =h[i]
            idx = i
    used[idx] =1
    print(h[idx])
