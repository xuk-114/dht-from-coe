n,m = map(int,input().split())
num = list(map(int,input().split()))
dp = [float('inf')]*(m+1)
dp[0] = 0
for i in num:
    dp[i] = 1
    for j in range(i,m+1):
        dp[j] = min(dp[j],dp[j-i]+1)
if dp[m] == float('inf'):
    print(-1)
else:
    print(dp[m])