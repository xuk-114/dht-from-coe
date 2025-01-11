while True:
    n,m = map(int,input().split())
    if n == m == 0:
        break
    s = list(map(int,input().split()))
    a = s[:n]
    c = s[n-1:-1]
    