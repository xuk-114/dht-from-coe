t,k = map(int,input().split())
n = 100001
m = 1000000007
dp = [0] * n
s = [0] * n
dp[0] = 1
for i in range(1,n):
    dp[i] = dp[i-1]
    if i>= k:
        dp[i] = (dp[i-1] +dp[i-k]) % m
    s[i] = (s[i-1] +dp[i] ) % m
for _ in range(t):
    a,b = map(int,input().split())
    print((s[b]-s[a-1]+m)%m)
