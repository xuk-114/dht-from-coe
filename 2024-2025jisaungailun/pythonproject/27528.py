n = int(input())
dp = [0]*(n+1)
dp[1] = 1
if n==1:
    print(1)
else:
    for i in range(2,n+1):
        for j in range(1,i):
            dp[i] += dp[j]
        dp[i] += 1
    print(dp[n])