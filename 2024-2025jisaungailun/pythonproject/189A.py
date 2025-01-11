n,a,b,c = map(int,input().split())
dp = [0]*(max(n,a,b,c)+1)
dp[a]=1
dp[b]=1
dp[c]=1
num = [a,b,c]
num.sort()
sp = [False] * (n + 1)
sp[0] = True  # 基础情况

for i in range(1, n + 1):
    if i >= a and sp[i - a]:
        sp[i] = True
    if i >= b and sp[i - b]:
        sp[i] = True
    if i >= c and sp[i - c]:
        sp[i] = True
for i in range(num[0],n+1,1):

    if i-num[1]<=0:
        dp[i] = max(dp[i],dp[i-num[0]]+1)
    elif i-num[1]>=1 and i-num[2]<=0:
        dp[i] = max(dp[i],dp[i-num[0]]+1,dp[i-num[1]]+1)
    elif i -num[2]>=1:
        dp[i] = max(dp[i],dp[i-num[0]]+1,dp[i-num[1]]+1,dp[i-num[2]]+1)
    if sp[i]:
        dp[i] = dp[i]
    else:
        dp[i] = 0
print(dp[n])


